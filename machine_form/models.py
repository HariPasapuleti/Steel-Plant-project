from django.db import models
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import qrcode
from django.core.files import File
import os

class Machine(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    company = models.CharField(max_length=255, default="")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='machine_images/', null=True, blank=True)
    qr_code = models.ImageField(blank=True, upload_to='qrCode')
    complaints = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.model}"
    
    def save(self, *args, **kwargs):

        # Delete the previous QR code file if it exists
        if self.pk:  # Ensure the instance already exists in the database
                old_qr = Machine.objects.filter(pk=self.pk).values_list('qr_code', flat=True).first()
                if old_qr:  # Check if an old QR code exists
                    try:
                        old_qr_path = self.qr_code.storage.path(old_qr)
                        if os.path.exists(old_qr_path):  # Ensure the file exists
                            os.remove(old_qr_path)  # Delete the file
                            print(f"Deleted old QR code: {old_qr_path}")
                    except Exception as e:
                        print(f"Error deleting old QR code: {e}")
        # Define the machine details for QR code content

        qr_content = (
            f"Machine Name: {self.name}\n"
            f"Model: {self.model}\n"
            f"Company: {self.company}\n"
            f"Latitude: {self.latitude}\n"
            f"Longitude: {self.longitude}\n"
            f"Description: {self.description}\n"
            f"Complains: {self.complaints}\n"
        )

        # Create QR code with larger box_size for better clarity
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=15,  # Increased box size for better clarity
            border=4,
        )
        qr.add_data(qr_content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # Create a larger canvas to ensure full visibility
        canvas_width, canvas_height = qr_image.size[0] + 40, qr_image.size[1] + 80
        qr_canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
        qr_canvas.paste(qr_image, (20, 60))  # Padded placement for clarity

        # Draw text at the top of the QR code
        draw = ImageDraw.Draw(qr_canvas)
        try:
            font = ImageFont.truetype("arial.ttf", 24)  # Larger font for clarity
        except IOError:
            font = ImageFont.load_default()

        # Add centered title text
        title_text = f"{self.name} - {self.model}"
        text_bbox = draw.textbbox((0, 0), title_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        draw.text(
            ((canvas_width - text_width) // 2, 20),
            title_text,
            font=font,
            fill="black"
        )

        # Save to a BytesIO stream
        stream = BytesIO()
        qr_canvas.save(stream, 'PNG')
        file_name = f'{self.name}_qr.png'
        
        # Save the QR code to the model field
        self.qr_code.save(file_name, File(stream), save=False)
        qr_canvas.close()
        
        super().save(*args, **kwargs)
