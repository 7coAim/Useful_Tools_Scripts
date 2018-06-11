'Internet Explorerで閲覧中のURLとタイトルのすべて取得
set fso = CreateObject("Scripting.FileSystemObject")
txt = ""
for each br in CreateObject("Shell.Application").Windows
  pname = fso.GetFileName( br.FullName )
  if  LCase( pname ) = "iexplore.exe" then
   if br.LocationURL <> "about:blank" then
    'Webサイトのタイトル
    txt = txt & br.Document.Title & vbcrlf
    ’WebサイトのURL
    txt = txt & br.LocationURL & vbcrlf & vbcrlf
   end if
  end if
next
wscript.echo txt
ClipBoardSet txt
 
'クリップボードへアクセスし貼付利用を可能にする
sub ClipBoardSet( s )
 Set objIE = CreateObject("InternetExplorer.Application")
 objIE.Navigate("about:blank")
 objIE.document.parentwindow.clipboardData.SetData "text", s
 objIE.Quit
 set objIE = Nothing
end sub
