# 简单扫雷

## 内容
`msw.py`是扫雷程序，运行需带上`img`文件夹  
运行`make_inlined.bat`生成内联资源版扫雷程序`msw_ires.py`，单文件即可运行  

## 运行环境
`python >= 3.6`  
依赖以下库：  
```
tkinter
pillow
numpy
```

## 外观自定义
### 按钮大小
找到`msw.py`中的这一行：  
```python
class MainWin:
```
修改它下面的两行：  
```python
    FIELD_BUTTON_SIZE = 20 # 扫雷场地按钮大小
    FACE_BUTTON_SIZE = 40 # 笑脸按钮大小
```
### 图片
替换`img`中的图片即可，会自动缩放。  

## 初始参数自定义
注：参数可以在启动后用UI调整。  
找到`msw.py`中的这一行：  
```python
if __name__ == '__main__':
```
修改它下面的一行：  
```python
    main = MainWin(20, 20, 96, 2 * 60)
```
四个入参为行数、列数、雷数、限时（小于等于0为不限时）  

