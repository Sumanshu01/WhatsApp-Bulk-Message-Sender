import pywhatkit as kit
import time

# List of phone numbers with country codes
numbers = [
'+918006526404', '+917002045044', 
'+917638041168', '+917708748744', '+917739755188', '+917888339374', '+917896423876', '+917898205526', 
'+917903699124', '+917904524063', '+917973517245', '+917974350674', '+917986979745', '+917994541755', 
'+918006526404'
]
# WE CAN ADD HERE AS MANY AS NUMBERS WE WANT
# Your message
message = "Why to choose us:- \n 1- Assignments available for all Subjects \n 2- Expert Help \n 3- 100% Quality Assurance \n 4- Affordable Charges \n 5- ON Time Delivery \n\nWhy struggling against your assignments/projects and all academic workload!!😩📚 \n\nJust Contact us and have your solution.✅✨"

# Path to the image file
image_path = r"image.jpg"  # Replace with the path to your image

# Sending message and image to each number
for number in numbers:
    try:
        print(f"Sending message with image to {number}...")
        kit.sendwhats_image(receiver=number, img_path=image_path, caption=message, wait_time=20)
        time.sleep(20)  # Wait to ensure the message is sent before sending the next
        print(f"Message successfully sent to {number}!")
    except Exception as e:
        print(f"Failed to send message to {number}. Error: {e}")
        time.sleep(10)  # Pause briefly before retrying or moving to the next number
