; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "juice"
#define MyAppVersion "1.0"
#define MyAppPublisher "zfshe"
#define MyAppURL "https://www.zfsya.com/"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{ED522828-CE0F-4FC8-8B05-3862CE8686AC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=D:\{#MyAppName}
DisableDirPage=yes
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=E:\winloc\Desktop\juice
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"

[Files]
Source: "E:\winloc\Desktop\juice\7z.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\winloc\Desktop\juice\juice.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[registry]
;���δ���������ע����еļ�ֵ
Root:HKCR;Subkey:*\shell\juice;ValueType: string; ValueName:MUIVerb;ValueData:ʹ��Juice���н�ѹ;Flags: uninsdeletekey
Root:HKCR;Subkey:*\shell\juice;ValueType: string; ValueName:Icon;ValueData:D:\juice\juice.exe ,0;Flags: uninsdeletekey
Root:HKCR;Subkey:*\shell\juice\command;ValueType: string; ValueName:;ValueData:D:\juice\juice.exe %1;Flags: uninsdeletekey