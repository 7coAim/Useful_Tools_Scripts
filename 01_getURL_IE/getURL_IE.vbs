'Internet Explorer�ŉ{������URL�ƃ^�C�g���̂��ׂĎ擾
set fso = CreateObject("Scripting.FileSystemObject")
txt = ""
for each br in CreateObject("Shell.Application").Windows
  pname = fso.GetFileName( br.FullName )
  if  LCase( pname ) = "iexplore.exe" then
   if br.LocationURL <> "about:blank" then
    'Web�T�C�g�̃^�C�g��
    txt = txt & br.Document.Title & vbcrlf
    �fWeb�T�C�g��URL
    txt = txt & br.LocationURL & vbcrlf & vbcrlf
   end if
  end if
next
wscript.echo txt
ClipBoardSet txt
 
'�N���b�v�{�[�h�փA�N�Z�X���\�t���p���\�ɂ���
sub ClipBoardSet( s )
 Set objIE = CreateObject("InternetExplorer.Application")
 objIE.Navigate("about:blank")
 objIE.document.parentwindow.clipboardData.SetData "text", s
 objIE.Quit
 set objIE = Nothing
end sub
