# Text into images
The basic idea behind this little project is to give a visual rappresentation of a text file in terms of an image. 



### image-encoder
The conversion task is achieved by taking a text file, extracting from it the single bits, and then writing them as pixels in an image (where a 1 is mapped into white and a 0 is mapped into black).
Further blank space in the image is filled with black. 

Note that the image is a png, and it's crucial for the purpose of the project that no kind of compression has to be applied on it.



### image-decoder
Moreover, it's also possible to reverse the process by taking the encoded image, extracting from it the pixels, converting them into bits and writing them on a text file.


### Examples
The image below is the result of the encoding of the first Canto of "Divina Commedia" (The Divine Commedy) by Dante Alighieri.

<img width="332" alt="divine_commedy" src="https://github.com/leonardobertolani/text-into-images/assets/102794282/67897023-dd6a-4091-a77c-06ea47088c71">
