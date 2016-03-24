
a = """

"""


import pickle


print a.split()

file_name = 'test_file.data'

fileObject = open(file_name, 'wb')

pickle.dump(a, fileObject)
fileObject.close()
print 'File Written '





'''
it crops and saves the image without background


            mask2 = np.zeros(im.shape[:2], np.uint8)
            bgdModel = np.zeros((1, 65),np.float64)
            fgdModel = np.zeros((1, 65),np.float64)

            rect = (x, y, w, h)
            cv2.grabCut(im,mask2,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)
            mask3 = np.where((mask2==2)|(mask2==0),0,1).astype('uint8')

            
            
            img = im * mask3[:,:,np.newaxis]
        
            
            bar = np.zeros((img.shape[0],5,3),np.uint8)
            output = np.zeros(im.shape,np.uint8) 
            res = np.hstack((img, output))
            plt.imshow(im),plt.colorbar(),plt.show()
            
            increment = increment + 1
            

'''