import cv2

def createImageObj(imgPath):
    img = cv2.imread(imgPath)
    return img

def blurImage(imgObj):
    blurImg = cv2.blur(imgObj, (10, 10))
    return blurImg

def resizeImage(bluredImageObj, reqDim):
    STD_Dimensions = {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160)
    }

    print("=> Original Dimension:", bluredImageObj.shape)
    
#    scale_percent = 220
#    width = int(bluredImageObj.shape[1] * scale_percent / 100)
#   height = int(bluredImageObj.shape[0] * scale_percent / 100)
    resDim = STD_Dimensions[reqDim] # resized Dimension

    # resize image
    resizedImg = cv2.resize(bluredImageObj, resDim, interpolation = cv2.INTER_AREA)
    print("=> Resized Dimension:", resizedImg.shape)

    return resizedImg

def buildBackgroundOverlay(background, overlay):
    return resultImage

if __name__ == "__main__":
    print("{0:=^39}".format("Hello to BluRo Engine"))

    imgPath = input("Enter path to image: ")
    reqDim = input("Enter dimension: ")

    # Create an Image object
    imgObj = createImageObj(imgPath)
    # Blur Image
    backgroundImage = blurImage(imgObj)
    # resize Image
    backgroundImage = resizeImage(backgroundImage, reqDim)
    # bring background and image together
    resultImage = buildBackgroundOverlay(backgroundImage, imgObj)

    cv2.imshow("Result Image", resultImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# D:\Gon.vlad\Programming\Python\BluRo\Engine\Samples\__Nature_2.jpg