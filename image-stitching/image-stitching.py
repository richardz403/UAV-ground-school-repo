import cv2


def main():

    vid = cv2.VideoCapture("Minecraft_stitch_test.mp4")

    frames = []
    cnt = 0

    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if(cnt%10 == 0):
            frames.append(frame)
        
        cnt += 1

        if cv2.waitKey(1) == ord('q'):
            break
    
    vid.release()
    cv2.destroyAllWindows()
    
    stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)
    status, pano = stitcher.stitch(frames)

    print(status)

    if status != cv2.Stitcher_OK:
        print("Can't stitch images, error code = %d" % status)
        return
 
    cv2.imshow('frame', pano)
 
    if cv2.waitKey(0) == ord('q'):
        print('Done')


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()