Title: Enable .NET Framework using Powershell
Date: 2020-08-25 10:58
Category: IT Notes
Cover: static/asp_net.png

Sometimes you cannot simply enable .NET tools from the control panel, this causes problems when working on projects in Visual Studio.
To fix this you need to download a new iso file using <a href='https://www.microsoft.com/en-us/software-download/windows10' target='_blank'>the Windows 10 media creation tool</a>. After downloading the iso from Microsoft, right click the file to mount the disk.
Next find the folder sources/sxs in the mounted iso. Then run below command.

`dism /online /enable-feature /featurename:NetFx3 /All /Source:/path/to/sources/sxs /LimitAccess`

*You'll have to replace /path/to/sources/sxs with your own path.*