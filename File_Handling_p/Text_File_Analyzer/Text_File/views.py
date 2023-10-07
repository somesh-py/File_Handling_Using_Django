from django.shortcuts import render

# Create your views here.

def Text(request):
    return render(request,'Text.html')

def Create(request):
    return render(request,'All_Operations.html',{'Create':'Create'})

def Create_requeest(request):
    if request.method=='POST':
        file_path=request.POST['file_Path']
        file_name=request.POST['file_Name']
        print('run')
        try:
            if not file_path:
                return render(request,'Text.html', {'emsgs': 'Enter Path'})

            elif not file_name:
                return render(request,'Text.html', {'emsgs': 'Enter File Name'})

            else:
                open(file_path + '/' + file_name, "x")
                print('File created successfully')
                return render(request, 'Text.html', {'msgs': 'File created successfully'})

        except FileExistsError:
            return render(request,'Text.html', {'emsgs': 'File Already Exists'})
        
        except PermissionError:
            return render(request,'Text.html', {'emsgs': 'Enter Path and File Name'})
        
        except FileNotFoundError:
            return render(request,'Text.html', {'emsgs': 'File Note Found'})

def Read(request):
    return render(request,'All_Operations.html',{'Read':'Read'})

def Read_Update_Data(request):
        return render(request,'Read_Update_Data.html')

def Read_request(request):
    if request.method=='POST':
        file_path=request.POST['file_Path']
        file_name=request.POST['file_Name']

        f=open(file_path+'/'+file_name,"r")
        file_data=f.read()
        print(file_data)
        return render(request,'Read_Update_Data.html',{'file_data':file_data})

def Write(request):
    return render(request,'All_Operations.html',{'Write':'Write'})

def Write_request(request):
    if request.method=='POST':
        file_path=request.POST['file_Path']
        file_name=request.POST['file_Name']
        file_data=request.POST['file_data']

        f=open(file_path+'/'+file_name,"w")
        f.write(file_data)
        print('data written sucessfully')
        return render(request,'Text.html',{'msgs':'Data Written Sucessfully'})

def Update(request):
    return render(request,'All_Operations.html',{'Update':'Update'})

def Delete(request):
    return render(request,'All_Operations.html',{'Delete':'Delete'})

def All_Operations(request):
    return render(request,'All_Operations.html')