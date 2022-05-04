# YOLO X on Google Colaboratory

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/husty530/Yamashita-yolox/blob/master/YOLOX-Training.ipynb)
  
当リポジトリではLinux環境(Google Colab)でのビルドを想定して、簡単にセットアップができるようにPyTorchのYOLOXソースコードを配置しています。  
ブラウザさえあれば誰でも動かせますので、以下の手順でやってみましょう。  

## つかいかた  
1. [YOLOX-Training.ipynb](/YOLOX-Training.ipynb)をGoogle Colaboratoryで開きます。ipynbはDriveに置くでも上のバッジから開くでもいいです。
2. ランタイムのタイプを"GPU"に変更し、自分のDriveをマウントします。次行、そこにこのリポジトリをクローンしましょう。
3. [workspace](/workspace)内にフォルダを作り、[pumpkin_640_480](/workspace/pumpkin_640_480)を参考に画像とラベルのフォルダを作ります。対応する画像とラベルの名前は必ず同じにしてください。(ちなみにこれはDarknetの作法です。兄弟リポジトリ[Yamashita-darknet](https://github.com/husty530/Yamashita-darknet)に合わせているためこうなっています)
4. [.names](/workspace/pumpkin_640_480/.names)を編集して、作成したフォルダに置きます。検出したいクラス数だけ改行しながらラベル名を書いてください。
5. ノートブックのconfigと書いてあるエリアでクラス数や画像サイズなどを適切に指定してください。
6. 上からポチポチしていきます。学習開始して、ザーッと画面が流れ始めたら成功です。
7. 終わったら、モデルを使って評価実行してみましょう。自分のフォルダに生成された"モデル名.pts"が最終成果物です。

.pts, .onnx 形式での保存ができるので、ダウンロードすればローカルでモデルを使用できます。PyTorchは付属のDemoプログラムのようなもので動きますし、
ONNXもPythonで[公式の実装例](https://github.com/Megvii-BaseDetection/YOLOX/blob/main/demo/ONNXRuntime/onnx_inference.py) があるのですぐに試せるかと思います。  
私のリポジトリ[Husty-public](https://github.com/husty530/Husty-public) ではC#のONNX Runtime経由でOpenCvSharpと連結したものを公開しています。

### ラベリング
正解ラベル付けはColabでなくローカル環境で行います。  
データフォーマットは物体一つにつきスペース区切りで(index) (x) (y) (width) (height)\nです。ただし、すべて画像の幅高さで割って0~1に丸めたものとなります。
ただのテキストファイルなので自作もできますが、[labelImg](https://github.com/tzutalin/labelImg)というフリーソフトが便利なのでそれを使いましょう。  
Python環境があるなら、pipコマンドが使える環境で
```
pip install labelImg
labelImg
```
だけで起動OK。一応ラベル名としてclasses.txtというファイルを置いとかないと動いてくれない仕様になっています。  
なんか怒られた場合は.namesと同じ内容をdatasetフォルダにコピーしてclasses.txtという名前にしてください。  
