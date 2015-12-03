; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{8267E060-07C7-4B7F-AD3F-73B38D8B8D0E}
AppName=CrageneRabbit
AppVersion=1.0
;AppVerName=CrageneRabbit 1.0
AppPublisher=WindowsHyun Company, Inc.
AppPublisherURL=http://www.windowshyun.co.kr
AppSupportURL=http://www.windowshyun.co.kr
AppUpdatesURL=http://www.windowshyun.co.kr
DefaultDirName={pf}\CrageneRabbit
DefaultGroupName=CrageneRabbit
OutputDir=C:\Users\WindowsHyun\Desktop
OutputBaseFilename=CrageneRabbit Installer
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\2DGraphics\2DGraphics\dist\CrageneRabbit.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\2DGraphics\2DGraphics\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\CrageneRabbit"; Filename: "{app}\CrageneRabbit.exe"
Name: "{commondesktop}\CrageneRabbit"; Filename: "{app}\CrageneRabbit.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\CrageneRabbit.exe"; Description: "{cm:LaunchProgram,CrageneRabbit}"; Flags: nowait postinstall skipifsilent

