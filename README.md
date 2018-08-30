# healing_fountain
噴水を見て癒やされるアプリ
## 使い方
main.jsから起動してください。
  - Space キーで噴水
  - q キー又は、EXITボタンで終了
## 注意点
tkinter で keyPress　が上手く機能しないので`os.system('xset r off')`でキーの連続入力をOFFにしています。
正常に終了しなかった場合この設定が残ってしまうので、'q キー' か 'EXITボタン' で終了してください。


もし設定が残ってしまった場合はpythonで`os.system('xset r on')`を実行するか、ログイン(PCを一旦スリープにする)し直したら元に戻ります。たぶん
