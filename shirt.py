import sys
from PIL import Image, ImageOps

if len(sys.argv)<3 :
    sys.exit('Too few command-line arguments')

elif len(sys.argv)>3 :
    sys.exit('Too many command-line arguments')

else :
    if sys.argv[1].lower().endswith(('.jpg', '.jpeg', '.png')) and sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png')) :
        if sys.argv[1].split('.')[1]==sys.argv[2].split('.')[1] :
            try :
                base=Image.open(sys.argv[1])
                overlay=Image.open('shirt.png')
                # overlay=overlay.resize((400,400))
                # print(overlay.size)
                # print(overlay.mode)
                # fit_overlay=ImageOps.fit(overlay,(400,400))
                # print(base.size)
                fit_base=ImageOps.fit(base,(600,600))
                fit_base.paste(overlay,(0,0),mask=overlay)
                fit_base.save(sys.argv[2])

            except FileNotFoundError :
                sys.exit('Could not find '+sys.argv[1])

        else :
            sys.exit('Input and output have different extensions')

    else :
        sys.exit('Invalid input')

# pillow has module Image and ImageOps
# Image has open() function and paste(), convert(), resize(), and save() method. also mode, size, and format attribute
# ImageOps has fit() function which crops to the desired dimensions. if image has 800x400 you want 400x400 it will crop
# centrally 200 from each side along the length and if it is 1600x800 then it will first crop to 800x800 then shrink.
# use centering like (0.5,0.0) to crop from top only
# resize() always shrinks or squishes distorting the proportions unlike fit()


