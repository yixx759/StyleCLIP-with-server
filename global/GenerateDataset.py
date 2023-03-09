from GenerateRand import mainhere

for i in range(10):
    filename = "Latent" + str(i)+".pt"
    photoname = str(i) +".jpg"
    mainhere("./Dataset/Photos/","./Dataset/Latents/"+filename,photoname)