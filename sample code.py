from codecs import BOM32_BE
 from ctypes import alignment
 from unittest import result
 from xml . dom . expatbuilder import parseString
 import numpy as np
 import pandas as pd
 import pydicom as dicom
 import os
 import matplotlib . pyplot as plt
 import cv2
 import math

 import tensorflow . api . v2 . compat . v1 as tf
 t f . disable_v2_behavior ( )
 import pandas as pd
 import tflearn
from tflearn . layers . conv import conv 3d , max pool 3d
from t f l e a r n . l a y e r s . c o r e i m p o r t i n p u t d a t a , dropout , f u l l y c o n n e c t e d
from t f l e a r n . l a y e r s . e s t i m a t o r i m p o r t r e g r e s s i o n
20 i m p o r t numpy as np
21 i m p o r t m a t p l o t l i b . p y p l o t as p l t
22
23 from s k l e a r n . m e t r i c s i m p o r t c o n f u s i o n m a t r i x
24
25 from t k i n t e r i m p o r t *
26 from t k i n t e r i m p o r t messagebox , t t k
 i m p o r t t k i n t e r as t k
28 from PIL i m p o r t Image , ImageTk


31 c l a s s LCD CNN :
32 d e f i n i t ( s e l f , r o o t ) :
33 self . root = r o o t
34 self . root . geometry ( ” 1006 x500+0+0 ” )
35 self . root . r e s i z a b l e ( F a l s e , F a l s e )
36 self . r o o t . t i t l e ( ”Lung Cancer D e t e c t i o n ” )

38 img4=Image . open ( ” Images \Lung−Cancer − D e t e c t i o n . j p g ” )
39 img4=img4 . r e s i z e ( ( 1 0 0 6 , 5 0 0 ) , Image . ANTIALIAS )
40 s e l f . photoimg4 =ImageTk . PhotoImage ( img4 )

42 bg img= Label ( s e l f . r o o t , image= s e l f . photoimg4 )
43 bg img . p l a c e ( x =0 , y =50 , width =1006 , h e i g h t =500)

45 t i t l e l b l = Label ( t e x t =”Lung Cancer D e t e c t i o n ” , f o n t =( ” B r a d l e y Hand ITC” , 3 0 , ” b old ” ) , bg=” b l a c k ” ,
fg =” w h i t e ” , )
46 t i t l e l b l . p l a c e ( x =0 , y =0 , width =1006 , h e i g h t =50)


48 s e l f . b1= B u t t o n ( t e x t =” I m p o r t Data ” , c u r s o r =” hand2 ” , command= s e l f . i m p o r t d a t a , f o n t =( ” Times New
Roman” , 1 5 , ” bo ld ” ) , bg=” w h i t e ” , fg =” b l a c k ” )
49 s e l f . b1 . p l a c e ( x =80 , y =130 , width =180 , h e i g h t =30)

51 s e l f . b2= B u t t o n ( t e x t =” Pre − P r o c e s s Data ” , c u r s o r =” hand2 ” , command= s e l f . p r e p r o c e s s d a t a , f o n t =( ”
Times New Roman” , 1 5 , ” b old ” ) , bg=” w h i t e ” , fg =” b l a c k ” )
52 s e l f . b2 . p l a c e ( x =80 , y =180 , width =180 , h e i g h t =30)
53 s e l f . b2 [ ” s t a t e ” ] = ” d i s a b l e d ”
54 s e l f . b2 . c o n f i g ( c u r s o r =” arrow ” )

56 s e l f . b3= B u t t o n ( t e x t =” T r a i n Data ” , c u r s o r =” hand2 ” , command= s e l f . t r a i n d a t a , f o n t =( ” Times New
Roman” , 1 5 , ” bo ld ” ) , bg=” w h i t e ” , fg =” b l a c k ” )
57 s e l f . b3 . p l a c e ( x =80 , y =230 , width =180 , h e i g h t =30)
58 s e l f . b3 [ ” s t a t e ” ] = ” d i s a b l e d ”
59 s e l f . b3 . c o n f i g ( c u r s o r =” arrow ” )
60 d e f i m p o r t d a t a ( s e l f ) :
61 s e l f . d a t a D i r e c t o r y = ’ s a m p l e i m a g e s / ’
62 s e l f . l u n g P a t i e n t s = os . l i s t d i r ( s e l f . d a t a D i r e c t o r y )

64 s e l f . l a b e l s = pd . r e a d c s v ( ’ s t a g e 1 l a b e l s . csv ’ , i n d e x c o l =0)

66 s e l f . s i z e = 10

68 s e l f . N o S l i c e s = 5

70 messagebox . showinfo ( ” I m p o r t Data ” , ” Data I m p o r t e d S u c c e s s f u l l y ! ” )