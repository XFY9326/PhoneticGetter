# PhoneticGetter
从本地词典与有道批量获取英语音标  
Get phonetic from local dictionary and youdao

## 使用步骤：
1. 新建Excel文件，将需要处理的单词依次放在默认工作簿的第一列，不需要任何抬头与样式
2. 另存为Excel，保存的文件类型选择“使用逗号分隔的csv”或者任何其它csv格式的文件
3. 将csv文件放到input目录下
4. 运行音标获取程序，保证运行过程中联网
5. 处理结束的csv文件以相同的文件名称放在output目录中
6. 使用Excel可以直接打开csv文件（或者选择打开方式中指定Excel打开），然后进行后续处理

- 注：input与output文件夹中的test.csv文件是作为测试用例存在的，不需要的话可以删除


    PhoneticGetter
    Copyright (C) 2020  XFY9326

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.