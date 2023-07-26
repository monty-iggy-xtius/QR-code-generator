import qrcode
import random


banner = """                     
                       ___  _____                     
                     .'/,-Y"     "~-.              
                     l.Y             ^.           
                     /\               _\_           
                    i            ___/"   "\                 
                    |          /"   "\   3 !                   
                    l         ]     3 !__./                 
                     \ _  _    \.___./    "~\                  
                      X \/ \            ___./                   
                     ( \ ___.   _..--~~"   ~`-.              
                      ` Z,--   /               \              
                        \__.  (   /       ______)            
                          \   l  /-----~~" /                
                           Y   \          /             
                           |    "x______.^             
                           |           \               
                           |            \              

    ░░▀░░█▀▀█░░░█▀▀█░█▀▀▄░░░█▀▀▀░█▀▀░█▀▀▄░█▀▀░█▀▀▄░█▀▀▄░▀█▀░▄▀▀▄░█▀▀▄
    ░░█▀░░▒▀▄░░░█▄▄█░█▄▄▀░░░█░▀▄░█▀▀░█░▒█░█▀▀░█▄▄▀░█▄▄█░░█░░█░░█░█▄▄▀
    ░▀▀▀░█▄▄█░░░░░░█░▀░▀▀░░░▀▀▀▀░▀▀▀░▀░░▀░▀▀▀░▀░▀▀░▀░░▀░░▀░░░▀▀░░▀░▀▀

    [+] A tool to help you easily create QR codes for all your data!
        find me --> https://github.com/monty-xtius/

                             i3

"""

def make_my_qrcode(context, name):
    colors = ["#6c757d", "#446592", "#3f3f3f", "#000000", "#060608", "#0b022d", "#1a273a"]

    #create a QRCode object where we specify some error correction, size of image, border around image
    qrcodeObject = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
        )
    #add what you may to the qrcode
    qrcodeObject.add_data(context)
    
    qrcodeObject.make(fit=True)
    
    #make the qrcode with colors specified
    image_to_save = qrcodeObject.make_image(fill_color=random.choice(colors), back__color="#000")
    #save the qrcode to a provided name
    image_to_save.save(name)

    print(f"Thank you for choosing us! Your data has been saved to {name}")


def get_data():
    print(banner)
    user_input = input("[+] Data to put in QRCode: ").strip()
    image_ = input("[+] How do you wish to save this QRCode: ").strip()

    #check for user provided image name else rename output image to data.png
    image_name = image_ if len(image_) > 4 else "data.png"

    #check if provided output path has an image extension else append a PNG
    image_ext = ["" if len(image_name.split(".")) > 1 else ".png"]
    
    #add the extension to the image output
    final_image_name = image_name + image_ext[0]

    make_my_qrcode(context=user_input, name=final_image_name)
                                            
if __name__ == '__main__':
    get_data()
