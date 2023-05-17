import kivy
from kivy.config import Config
kivy.require('1.10.1')
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '760')
from kivy.app import App
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
Window.clearcolor = (.3, .3, .3, 1)

import numpy

import pandas as pd
    
import sqlite3

import random as rand


conn = sqlite3.connect('KanjidbSheets.db')

kanjiList = pd.read_sql_query("SELECT * FROM KLAL6QuizSet", conn)
print(kanjiList)
conn.close()


kanjiList = kanjiList.to_numpy()
kanjiList = list(kanjiList)
rand.shuffle(kanjiList)


kanjiIndex = 0

class KanjiScreen(Screen):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)


    def kanjiNext(self):
        global kanjiIndex

        if kanjiIndex != len(kanjiList) - 1:
            kanjiIndex = kanjiIndex + 1
        else:
            rand.shuffle(kanjiList)
            for i in range(len(kanjiList)):

                if kanjiList[i][3] == 1:
                    kanjiList.insert(0, kanjiList.pop(i))
            kanjiIndex = -1
            

    
    def shuffleSet(self):
            global kanjiIndex
            rand.shuffle(kanjiList)
            for i in range(len(kanjiList)):
                if kanjiList[i][3] == 1:
                    kanjiList.insert(0, kanjiList.pop(i))
            kanjiIndex = -1


            

class DrawingPad(Widget):
    

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas.after:
                Color(0, 0, 0)
                d = 10
                Ellipse(pos = (touch.x - d/2, touch.y - d/2), size = (d,d))


    def ClearPad(self):
        with self.canvas.after:
            self.canvas.after.clear()
            

class kanjiLabel(Label):
    
    def kanjiLabelChange(self):
        global kanjiIndex
        self.text = kanjiList[kanjiIndex][0]

    def kanjiLabelClear(self):
        self.text = ""


class hiraganaLabel(Label):
    
    def hiraganaLabelChange(self):
        global kanjiIndex
        self.text = kanjiList[kanjiIndex][1]


class englishLabel(Label):

    def englishLabelChange(self):
        global kanjiIndex
        self.text = kanjiList[kanjiIndex][2]


class favBut(Button):
    

    def checkFav(self):
        if kanjiList[kanjiIndex][3] == 0:
            self.color = (1, 1, 1)
        else:
            self.color = (1, 1, 0)

    def setFav(self):
        global kanjiIndex
       
        if kanjiList[kanjiIndex][3] == 0:
            kanjiList[kanjiIndex][3] = 1
            self.color = (1, 1, 0)
        else:
            kanjiList[kanjiIndex][3] = 0
            self.color = (1, 1, 1)






class KanjiKVApp(App):

    kv_directory = 'C:\\Users\\nrmyn\\OneDrive\\Documents\\KanjiApp'
    

    
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainScreen(name='Main'))
        sm.add_widget(KanjiScreen(name='Kanji'))

        return sm
    




if __name__ == '__main__':
    KanjiKVApp().run()



# Kivy Libraries Licensing:

#Copyright (c) 2010-2023 Kivy Team and other contributors

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
#https://github.com/kivy/kivy/blob/master/LICENSE


# Pygments Library Licensing

#Copyright (c) 2006-2022 by the respective authors (see AUTHORS file).
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are
#met:

#* Redistributions of source code must retain the above copyright
#  notice, this list of conditions and the following disclaimer.

#* Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# The OpenGL Extension Wrangler Library Licensing:

#Copyright (C) 2008-2016, Nigel Stewart <nigels[]users sourceforge net>
#Copyright (C) 2002-2008, Milan Ikits <milan ikits[]ieee org>
#Copyright (C) 2002-2008, Marcelo E. Magallon <mmagallo[]debian org>
#Copyright (C) 2002, Lev Povalahev
#All rights reserved.

#Redistribution and use in source and binary forms, with or without 
#modification, are permitted provided that the following conditions are met:

#* Redistributions of source code must retain the above copyright notice, 
#  this list of conditions and the following disclaimer.
#* Redistributions in binary form must reproduce the above copyright notice, 
#  this list of conditions and the following disclaimer in the documentation 
#  and/or other materials provided with the distribution.
#* The name of the author may be used to endorse or promote products 
#  derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
#LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
#CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
#SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#THE POSSIBILITY OF SUCH DAMAGE.






# Numpy Library Licensing:

#Copyright (c) 2005-2022, NumPy Developers.
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are
#met:

#    * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.

#    * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.

#    * Neither the name of the NumPy Developers nor the names of any
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#https://numpy.org/doc/stable/license.html



# Pandas Library Licensing:

#BSD 3-Clause License

#Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
#All rights reserved.

#Copyright (c) 2011-2023, Open source contributors.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:

#* Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.

#* Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.

#* Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived from
#  this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#R TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
#
#https://github.com/pandas-dev/pandas/blob/main/LICENSE

# SQLite3 Library Licensing:

# SQLite3 is in the Public Domain and does not require attribution 
#
# https://www.sqlite.org/copyright.html


# Random Library Licensing:

#MIT License

#Copyright (c) 2017 Maxim

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.