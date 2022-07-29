from django.utils import timezone
from django.http import JsonResponse
from django.views import View
import json
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from class_booker.forms import BookingRequest
from class_booker.models import Booking


teacher_availability = settings.TEACHER_AVAILABILITY

@method_decorator(csrf_exempt, name='dispatch')
class BookClass(View):

    def send_email_to_student(self, booking_data, booking_date):
        send_mail(
            'Booked Class Details',
            f"Dear {booking_data['full_name']}, Your class with " + \
            f"{teacher_availability['full_name']} has been booked for " + \
            f"{booking_date.strftime('%d %B %Y')} from {booking_data['start_time']} to " + \
            f"{booking_data['end_time']}.",
            teacher_availability['email'], # sender email address
            [booking_data['email_address']], # receiver email address
            fail_silently=True,
        )

    def get_next_available_class(self, booking_data):
        try:
            last_booking = Booking.objects.filter(date__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0), day=booking_data['weekday']).order_by('-date')[0]
            next_booking_time = last_booking.date + timezone.timedelta(days=7)
        except IndexError:
            next_booking_time = timezone.now()
            while(next_booking_time.strftime('%A') != booking_data['weekday'] or \
                next_booking_time < timezone.now()):
                next_booking_time = next_booking_time + timezone.timedelta(days=1)
        return next_booking_time


    def check_slot_exists(self, booking_data):
        requested_day = booking_data['weekday'].lower()
        available_days = [str.lower() for str in teacher_availability['availability'].keys()]
        if (requested_day in available_days):
            for slot_time in teacher_availability['availability'][requested_day]:
                if slot_time["start_time"].lower() == booking_data["start_time"].lower() and \
                    slot_time["end_time"].lower() == booking_data["end_time"].lower():
                        return True
        return False

    def book_slot(self, booking_data):
        if (self.check_slot_exists(booking_data)):
            next_avl_cls_date = self.get_next_available_class(booking_data)
            Booking.objects.create(
                date = next_avl_cls_date,
                day = booking_data["weekday"],
                start_time = booking_data["start_time"],
                end_time = booking_data["end_time"],
                teacher_full_name = teacher_availability['full_name'],
                teacher_email = teacher_availability['email'],
                student_full_name = booking_data['full_name'],
                student_email = booking_data['email_address']
            )
            self.send_email_to_student(booking_data, next_avl_cls_date)
            return JsonResponse({
                "slot_confirmed": True,
                "weekday": booking_data["weekday"],
                "start_time": booking_data["start_time"],
                "end_time": booking_data["end_time"],
                "date": next_avl_cls_date.strftime("%d %B %Y")
            })
        else:
            return JsonResponse({
                "slot_confirmed": "false",
                "reason": "teacher is not available on this day"
            })

    def post(self, request):
        try:
            received_json_data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({"reason": "malformed request data"}, status=400)
        bookingRequestForm = BookingRequest(received_json_data)

        if bookingRequestForm.is_valid():
            booking_data = bookingRequestForm.cleaned_data
            return self.book_slot(booking_data)
        else:
            return JsonResponse(bookingRequestForm.errors, status=400)

