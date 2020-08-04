import rasterio
import numpy as np
import pandas as pd

def non_zeros(input_tif):
    
    src = rasterio.open(input_tif)
    array = src.read(1)
    array2 = np.uint16(array)
    q = array2.reshape(-1, 1)
    

    df = pd.DataFrame(data = q)
    df.columns= ['band'+str(input_tif)[1:-4]]
    
    df2 = df.loc[(df!=0).any(axis=1)]

    return df2

def sort_tif():
	# In[97]:


	input_tif1 = '01.TIF'
	res1 = non_zeros(input_tif1)


	# In[349]:


	input_tif2 = '02.TIF'
	res2 = non_zeros(input_tif2)


	# In[99]:


	input_tif3 = '03.TIF'
	res3 = non_zeros(input_tif3)


	# In[ ]:





	# In[ ]:





	# In[100]:


	input_tif4 = '04.TIF'
	res4 = non_zeros(input_tif4)


	# In[101]:


	input_tif5 = '05.TIF'
	res5 = non_zeros(input_tif5)


	# In[102]:


	input_tif6 = '06.TIF'
	res6 = non_zeros(input_tif6)


	# In[103]:


	input_tif7 = '07.TIF'
	res7 = non_zeros(input_tif7)


	# In[104]:


	input_tif8 = '08.TIF'
	res8 = non_zeros(input_tif8)


	# In[105]:


	input_tif9 = '09.TIF'
	res9 = non_zeros(input_tif9)


	# In[106]:


	input_tif10 = '010.TIF'
	res10 = non_zeros(input_tif10)


	# In[107]:


	input_tif11 = '011.TIF'
	res11 = non_zeros(input_tif11)


	# In[108]:


	input_tif12 = '012.TIF'
	res12 = non_zeros(input_tif12)


	# In[109]:


	input_tif13 = '013.TIF'
	res13 = non_zeros(input_tif13)


	# In[110]:


	input_tif14 = '014.TIF'
	res14 = non_zeros(input_tif14)


	# In[111]:


	input_tif15 = '015.TIF'
	res15 = non_zeros(input_tif15)


	# In[112]:


	input_tif16 = '016.TIF'
	res16 = non_zeros(input_tif16)


	# In[113]:


	input_tif17 = '017.TIF'
	res17 = non_zeros(input_tif17)


	# In[114]:


	input_tif18 = '018.TIF'
	res18 = non_zeros(input_tif18)


	# In[115]:


	input_tif19 = '019.TIF'
	res19 = non_zeros(input_tif19)


	# In[116]:


	input_tif20 = '020.TIF'
	res20 = non_zeros(input_tif20)


	# In[117]:


	input_tif21 = '021.TIF'
	res21 = non_zeros(input_tif21)


	# In[118]:


	input_tif22 = '022.TIF'
	res22 = non_zeros(input_tif22)


	# In[119]:


	input_tif23 = '023.TIF'
	res23 = non_zeros(input_tif23)


	# In[120]:


	input_tif24 = '024.TIF'
	res24 = non_zeros(input_tif24)


	# In[121]:


	input_tif25 = '025.TIF'
	res25 = non_zeros(input_tif25)


	# In[122]:


	input_tif26 = '026.TIF'
	res26 = non_zeros(input_tif26)


	# In[123]:


	input_tif27 = '027.TIF'
	res27 = non_zeros(input_tif27)


	# In[124]:


	input_tif28 = '028.TIF'
	res28 = non_zeros(input_tif28)


	# In[125]:


	input_tif29 = '029.TIF'
	res29 = non_zeros(input_tif29)


	# In[126]:


	input_tif30 = '030.TIF'
	res30 = non_zeros(input_tif30)


	# In[127]:


	input_tif31 = '031.TIF'
	res31 = non_zeros(input_tif31)


	# In[128]:


	input_tif32 = '032.TIF'
	res32 = non_zeros(input_tif32)


	# In[129]:


	input_tif33 = '033.TIF'
	res33 = non_zeros(input_tif33)


	# In[130]:


	input_tif34 = '034.TIF'
	res34 = non_zeros(input_tif34)


	# In[131]:


	input_tif35 = '035.TIF'
	res35 = non_zeros(input_tif35)


	# In[132]:


	input_tif36 = '036.TIF'
	res36 = non_zeros(input_tif36)


	# In[133]:


	input_tif37 = '037.TIF'
	res37 = non_zeros(input_tif37)


	# In[134]:


	input_tif38 = '038.TIF'
	res38 = non_zeros(input_tif38)


	# In[135]:


	input_tif39 = '039.TIF'
	res39 = non_zeros(input_tif39)


	# In[136]:


	input_tif40 = '040.TIF'
	res40 = non_zeros(input_tif40)


	# In[137]:


	input_tif41 = '041.TIF'
	res41 = non_zeros(input_tif41)


	# In[138]:


	input_tif42 = '042.TIF'
	res42 = non_zeros(input_tif42)


	# In[139]:


	input_tif43 = '043.TIF'
	res43 = non_zeros(input_tif43)


	# In[140]:


	input_tif44 = '044.TIF'
	res44 = non_zeros(input_tif44)


	# In[141]:


	input_tif45 = '045.TIF'
	res45 = non_zeros(input_tif45)


	# In[142]:


	input_tif46 = '046.TIF'
	res46 = non_zeros(input_tif46)


	# In[143]:


	input_tif47 = '047.TIF'
	res47 = non_zeros(input_tif47)


	# In[144]:


	input_tif48 = '048.TIF'
	res48 = non_zeros(input_tif48)


	# In[145]:


	input_tif49 = '049.TIF'
	res49 = non_zeros(input_tif49)


	# In[146]:


	input_tif50 = '050.TIF'
	res50 = non_zeros(input_tif50)


	# In[147]:


	input_tif51 = '051.TIF'
	res51 = non_zeros(input_tif51)


	# In[148]:


	input_tif52 = '052.TIF'
	res52 = non_zeros(input_tif52)


	# In[149]:


	input_tif53 = '053.TIF'
	res53 = non_zeros(input_tif53)


	# In[150]:


	input_tif54 = '054.TIF'
	res54 = non_zeros(input_tif54)


	# In[151]:


	input_tif55 = '055.TIF'
	res55 = non_zeros(input_tif55)


	# In[152]:


	input_tif56 = '056.TIF'
	res56 = non_zeros(input_tif56)


	# In[153]:


	input_tif57 = '057.TIF'
	res57 = non_zeros(input_tif57)


	# In[154]:


	input_tif58 = '058.TIF'
	res58 = non_zeros(input_tif58)


	# In[155]:


	input_tif59 = '059.TIF'
	res59 = non_zeros(input_tif59)


	# In[156]:


	input_tif60 = '060.TIF'
	res60 = non_zeros(input_tif60)


	# In[157]:


	input_tif61 = '061.TIF'
	res61 = non_zeros(input_tif61)


	# In[158]:


	input_tif62 = '062.TIF'
	res62 = non_zeros(input_tif62)


	# In[159]:


	input_tif63 = '063.TIF'
	res63 = non_zeros(input_tif63)


	# In[160]:


	input_tif64 = '064.TIF'
	res64 = non_zeros(input_tif64)


	# In[161]:


	input_tif65 = '065.TIF'
	res65 = non_zeros(input_tif65)


	# In[162]:


	input_tif66 = '066.TIF'
	res66 = non_zeros(input_tif66)


	# In[163]:


	input_tif67 = '067.TIF'
	res67 = non_zeros(input_tif67)


	# In[164]:


	input_tif68 = '068.TIF'
	res68 = non_zeros(input_tif68)


	# In[165]:


	input_tif69 = '069.TIF'
	res69 = non_zeros(input_tif69)


	# In[166]:


	input_tif70 = '070.TIF'
	res70 = non_zeros(input_tif70)


	# In[167]:


	input_tif71 = '071.TIF'
	res71 = non_zeros(input_tif71)


	# In[168]:


	input_tif72 = '072.TIF'
	res72 = non_zeros(input_tif72)


	# In[169]:


	input_tif73 = '073.TIF'
	res73 = non_zeros(input_tif73)


	# In[170]:


	input_tif74 = '074.TIF'
	res74 = non_zeros(input_tif74)


	# In[171]:


	input_tif75 = '075.TIF'
	res75 = non_zeros(input_tif75)


	# In[172]:


	input_tif76 = '076.TIF'
	res76 = non_zeros(input_tif76)


	# In[173]:


	input_tif77 = '077.TIF'
	res77 = non_zeros(input_tif77)


	# In[174]:


	input_tif78 = '078.TIF'
	res78 = non_zeros(input_tif78)


	# In[175]:


	input_tif79 = '079.TIF'
	res79 = non_zeros(input_tif79)


	# In[176]:


	input_tif80 = '080.TIF'
	res80 = non_zeros(input_tif80)


	# In[177]:


	input_tif81 = '081.TIF'
	res81 = non_zeros(input_tif81)


	# In[178]:


	input_tif82 = '082.TIF'
	res82 = non_zeros(input_tif82)


	# In[179]:


	input_tif83 = '083.TIF'
	res83 = non_zeros(input_tif83)


	# In[342]:


	input_tif84 = '084.TIF'
	res84 = non_zeros(input_tif84)


	# In[181]:


	input_tif85 = '085.TIF'
	res85 = non_zeros(input_tif85)


	# In[182]:


	input_tif86 = '086.TIF'
	res86 = non_zeros(input_tif86)


	# In[183]:


	input_tif87 = '087.TIF'
	res87 = non_zeros(input_tif87)


	# In[184]:


	input_tif88 = '088.TIF'
	res88 = non_zeros(input_tif88)


	# In[185]:


	input_tif89 = '089.TIF'
	res89 = non_zeros(input_tif89)


	# In[186]:


	input_tif90 = '090.TIF'
	res90 = non_zeros(input_tif90)


	# In[187]:


	input_tif91 = '091.TIF'
	res91 = non_zeros(input_tif91)


	# In[188]:


	input_tif92 = '092.TIF'
	res92 = non_zeros(input_tif92)


	# In[189]:


	input_tif93 = '093.TIF'
	res93 = non_zeros(input_tif93)


	# In[190]:


	input_tif94 = '094.TIF'
	res94 = non_zeros(input_tif94)


	# In[191]:


	input_tif95 = '095.TIF'
	res95 = non_zeros(input_tif95)


	# In[192]:


	input_tif96 = '096.TIF'
	res96 = non_zeros(input_tif96)


	# In[193]:


	input_tif97 = '097.TIF'
	res97 = non_zeros(input_tif97)


	# In[194]:


	input_tif98 = '098.TIF'
	res98 = non_zeros(input_tif98)


	# In[195]:


	input_tif99 = '099.TIF'
	res99 = non_zeros(input_tif99)


	# In[196]:


	input_tif100 = '0100.TIF'
	res100 = non_zeros(input_tif100)


	# In[197]:


	input_tif101 = '0101.TIF'
	res101 = non_zeros(input_tif101)


	# In[198]:


	input_tif102 = '0102.TIF'
	res102 = non_zeros(input_tif102)


	# In[ ]:





	# In[199]:


	input_tif103 = '0103.TIF'
	res103 = non_zeros(input_tif103)


	# In[200]:


	input_tif104 = '0104.TIF'
	res104 = non_zeros(input_tif104)


	# In[201]:


	input_tif105 = '0105.TIF'
	res105 = non_zeros(input_tif105)


	# In[345]:


	input_tif106 = '0106.TIF'
	res106 = non_zeros(input_tif106)


	# In[346]:


	input_tif107 = '0107.TIF'
	res107 = non_zeros(input_tif107)


	# In[203]:


	input_tif108 = '0108.TIF'
	res108 = non_zeros(input_tif108)


	# In[204]:


	input_tif109 = '0109.TIF'
	res109 = non_zeros(input_tif109)


	# In[205]:


	input_tif110 = '0110.TIF'
	res110 = non_zeros(input_tif110)


	# In[206]:


	input_tif111 = '0111.TIF'
	res111 = non_zeros(input_tif111)


	# In[207]:


	input_tif112 = '0112.TIF'
	res112 = non_zeros(input_tif112)


	# In[208]:


	input_tif113 = '0113.TIF'
	res113 = non_zeros(input_tif113)


	# In[209]:


	input_tif114 = '0114.TIF'
	res114 = non_zeros(input_tif114)


	# In[210]:


	input_tif115 = '0115.TIF'
	res115 = non_zeros(input_tif115)


	# In[211]:


	input_tif116 = '0116.TIF'
	res116 = non_zeros(input_tif116)


	# In[212]:


	input_tif117 = '0117.TIF'
	res117 = non_zeros(input_tif117)


	# In[213]:


	input_tif118 = '0118.TIF'
	res118 = non_zeros(input_tif118)


	# In[214]:


	input_tif119 = '0119.TIF'
	res119 = non_zeros(input_tif119)


	# In[215]:


	input_tif120 = '0120.TIF'
	res120 = non_zeros(input_tif120)


	# In[216]:


	input_tif121 = '0121.TIF'
	res121 = non_zeros(input_tif121)


	# In[217]:


	input_tif122 = '0122.TIF'
	res122 = non_zeros(input_tif122)


	# In[218]:


	input_tif123 = '0123.TIF'
	res123 = non_zeros(input_tif123)


	# In[219]:


	input_tif124 = '0124.TIF'
	res124 = non_zeros(input_tif124)


	# In[220]:


	input_tif125 = '0125.TIF'
	res125 = non_zeros(input_tif125)


	# In[221]:


	input_tif126 = '0126.TIF'
	res126 = non_zeros(input_tif126)


	# In[222]:


	input_tif127 = '0127.TIF'
	res127 = non_zeros(input_tif127)


	# In[223]:


	input_tif128 = '0128.TIF'
	res128 = non_zeros(input_tif128)


	# In[224]:


	input_tif129 = '0129.TIF'
	res129 = non_zeros(input_tif129)


	# In[225]:


	input_tif130 = '0130.TIF'
	res130 = non_zeros(input_tif130)


	# In[226]:


	input_tif131 = '0131.TIF'
	res131 = non_zeros(input_tif131)


	# In[227]:


	input_tif132 = '0132.TIF'
	res132 = non_zeros(input_tif132)


	# In[228]:


	input_tif133 = '0133.TIF'
	res133 = non_zeros(input_tif133)


	# In[229]:


	input_tif134 = '0134.TIF'
	res134 = non_zeros(input_tif134)


	# In[230]:


	input_tif134 = '0134.TIF'
	res134 = non_zeros(input_tif134)


	# In[231]:


	input_tif135 = '0135.TIF'
	res135 = non_zeros(input_tif135)


	# In[232]:


	input_tif136 = '0136.TIF'
	res136 = non_zeros(input_tif136)


	# In[233]:


	input_tif137 = '0137.TIF'
	res137 = non_zeros(input_tif137)


	# In[234]:


	input_tif138 = '0138.TIF'
	res138 = non_zeros(input_tif138)


	# In[235]:


	input_tif139 = '0139.TIF'
	res139 = non_zeros(input_tif139)


	# In[236]:


	input_tif140 = '0140.TIF'
	res140 = non_zeros(input_tif140)


	# In[237]:


	input_tif141 = '0141.TIF'
	res141 = non_zeros(input_tif141)


	# In[238]:


	input_tif142 = '0142.TIF'
	res142 = non_zeros(input_tif142)


	# In[239]:


	input_tif143 = '0143.TIF'
	res143 = non_zeros(input_tif143)


	# In[240]:


	input_tif144 = '0144.TIF'
	res144 = non_zeros(input_tif144)


	# In[241]:


	input_tif145 = '0145.TIF'
	res145 = non_zeros(input_tif145)


	# In[242]:


	input_tif146 = '0146.TIF'
	res146 = non_zeros(input_tif146)


	# In[243]:


	input_tif147 = '0147.TIF'
	res147 = non_zeros(input_tif147)


	# In[244]:


	input_tif148 = '0148.TIF'
	res148 = non_zeros(input_tif148)


	# In[245]:


	input_tif149 = '0149.TIF'
	res149 = non_zeros(input_tif149)


	# In[246]:


	input_tif150 = '0150.TIF'
	res150 = non_zeros(input_tif150)


	# In[247]:


	input_tif151 = '0151.TIF'
	res151 = non_zeros(input_tif151)


	# In[248]:


	input_tif152 = '0152.TIF'
	res152 = non_zeros(input_tif152)


	# In[249]:


	input_tif153 = '0153.TIF'
	res153 = non_zeros(input_tif153)


	# In[250]:


	input_tif154 = '0154.TIF'
	res154 = non_zeros(input_tif154)


	# In[251]:


	input_tif155 = '0155.TIF'
	res155 = non_zeros(input_tif155)


	# In[252]:


	input_tif156 = '0156.TIF'
	res156 = non_zeros(input_tif156)


	# In[253]:


	input_tif157 = '0157.TIF'
	res157 = non_zeros(input_tif157)


	# In[254]:


	input_tif158 = '0158.TIF'
	res158 = non_zeros(input_tif158)


	# In[255]:


	input_tif159 = '0159.TIF'
	res159 = non_zeros(input_tif159)


	# In[256]:


	input_tif160 = '0160.TIF'
	res160 = non_zeros(input_tif160)


	# In[257]:


	input_tif161 = '0161.TIF'
	res161 = non_zeros(input_tif161)


	# In[258]:


	input_tif162 = '0162.TIF'
	res162 = non_zeros(input_tif162)


	# In[259]:


	input_tif163 = '0163.TIF'
	res163 = non_zeros(input_tif163)


	# In[260]:


	input_tif164 = '0164.TIF'
	res164 = non_zeros(input_tif164)


	# In[261]:


	input_tif165 = '0165.TIF'
	res165 = non_zeros(input_tif165)


	# In[262]:


	input_tif166 = '0166.TIF'
	res166 = non_zeros(input_tif166)


	# In[263]:


	input_tif167 = '0167.TIF'
	res167 = non_zeros(input_tif167)


	# In[264]:


	input_tif168 = '0168.TIF'
	res168 = non_zeros(input_tif168)


	# In[265]:


	input_tif169 = '0169.TIF'
	res169 = non_zeros(input_tif169)


	# In[266]:


	input_tif170 = '0170.TIF'
	res170 = non_zeros(input_tif170)


	# In[267]:


	input_tif171 = '0171.TIF'
	res171 = non_zeros(input_tif171)


	# In[268]:


	input_tif172 = '0172.TIF'
	res172 = non_zeros(input_tif172)


	# In[269]:


	input_tif173 = '0173.TIF'
	res173 = non_zeros(input_tif173)


	# In[270]:


	input_tif174 = '0174.TIF'
	res174 = non_zeros(input_tif174)


	# In[271]:


	input_tif175 = '0175.TIF'
	res175 = non_zeros(input_tif175)


	# In[272]:


	input_tif176 = '0176.TIF'
	res176 = non_zeros(input_tif176)


	# In[273]:


	input_tif177 = '0177.TIF'
	res177 = non_zeros(input_tif177)


	# In[274]:


	input_tif178 = '0178.TIF'
	res178 = non_zeros(input_tif178)


	# In[275]:


	input_tif179 = '0179.TIF'
	res179 = non_zeros(input_tif179)


	# In[276]:


	input_tif180 = '0180.TIF'
	res180 = non_zeros(input_tif180)


	# In[277]:


	input_tif181 = '0181.TIF'
	res181 = non_zeros(input_tif181)


	# In[278]:


	input_tif182 = '0182.TIF'
	res182 = non_zeros(input_tif182)


	# In[279]:


	input_tif183 = '0183.TIF'
	res183 = non_zeros(input_tif183)


	# In[280]:


	input_tif184 = '0184.TIF'
	res184 = non_zeros(input_tif184)


	# In[281]:


	input_tif185 = '0185.TIF'
	res185 = non_zeros(input_tif185)


	# In[282]:


	input_tif186 = '0186.TIF'
	res186 = non_zeros(input_tif186)


	# In[283]:


	input_tif187 = '0187.TIF'
	res187 = non_zeros(input_tif187)


	# In[284]:


	input_tif188 = '0188.TIF'
	res188 = non_zeros(input_tif188)


	# In[285]:


	input_tif189 = '0189.TIF'
	res189 = non_zeros(input_tif189)


	# In[286]:


	input_tif190 = '0190.TIF'
	res190 = non_zeros(input_tif190)


	# In[287]:


	input_tif191 = '0191.TIF'
	res191 = non_zeros(input_tif191)


	# In[288]:


	input_tif192 = '0192.TIF'
	res192 = non_zeros(input_tif192)


	# In[289]:


	input_tif193 = '0193.TIF'
	res193 = non_zeros(input_tif193)


	# In[290]:


	input_tif194 = '0194.TIF'
	res194 = non_zeros(input_tif194)


	# In[291]:


	input_tif195 = '0195.TIF'
	res195 = non_zeros(input_tif195)


	# In[292]:


	input_tif196 = '0196.TIF'
	res196 = non_zeros(input_tif196)


	# In[293]:


	input_tif197 = '0197.TIF'
	res197 = non_zeros(input_tif197)


	# In[294]:


	input_tif198 = '0198.TIF'
	res198 = non_zeros(input_tif198)


	# In[295]:


	input_tif199 = '0199.TIF'
	res199 = non_zeros(input_tif199)


	# In[296]:


	input_tif200 = '0200.TIF'
	res200 = non_zeros(input_tif200)


	# In[297]:


	input_tif201 = '0201.TIF'
	res201 = non_zeros(input_tif201)


	# In[298]:


	input_tif202 = '0202.TIF'
	res202 = non_zeros(input_tif202)


	# In[299]:


	input_tif203 = '0203.TIF'
	res203 = non_zeros(input_tif203)


	# In[300]:


	input_tif204 = '0204.TIF'
	res204 = non_zeros(input_tif204)


	# In[301]:


	input_tif205 = '0205.TIF'
	res205 = non_zeros(input_tif205)


	# In[302]:


	input_tif206 = '0206.TIF'
	res206 = non_zeros(input_tif206)


	# In[303]:


	input_tif207 = '0207.TIF'
	res207 = non_zeros(input_tif207)


	# In[348]:


	input_tif208 = '0208.TIF'
	res208 = non_zeros(input_tif208)


	# In[305]:


	input_tif209 = '0209.TIF'
	res209 = non_zeros(input_tif209)


	# In[306]:


	input_tif210 = '0210.TIF'
	res210 = non_zeros(input_tif210)


	# In[307]:


	input_tif211 = '0211.TIF'
	res211 = non_zeros(input_tif211)


	# In[308]:


	input_tif212 = '0212.TIF'
	res212 = non_zeros(input_tif212)


	# In[309]:


	input_tif213 = '0213.TIF'
	res213 = non_zeros(input_tif213)


	# In[310]:


	input_tif214 = '0214.TIF'
	res214 = non_zeros(input_tif214)


	# In[311]:


	input_tif215 = '0215.TIF'
	res215 = non_zeros(input_tif215)


	# In[312]:


	input_tif216 = '0216.TIF'
	res216 = non_zeros(input_tif216)


	# In[313]:


	input_tif217 = '0217.TIF'
	res217 = non_zeros(input_tif217)


	# In[314]:


	input_tif218 = '0218.TIF'
	res218 = non_zeros(input_tif218)


	# In[315]:


	input_tif219 = '0219.TIF'
	res219 = non_zeros(input_tif219)


	# In[316]:


	input_tif220 = '0220.TIF'
	res220 = non_zeros(input_tif220)


	# In[317]:


	input_tif221 = '0221.TIF'
	res221 = non_zeros(input_tif221)


	# In[318]:


	input_tif222 = '0222.TIF'
	res222 = non_zeros(input_tif222)


	# In[319]:


	input_tif223 = '0223.TIF'
	res223 = non_zeros(input_tif223)


	# In[320]:


	input_tif224 = '0224.TIF'
	res224 = non_zeros(input_tif224)


	# In[321]:


	input_tif225 = '0225.TIF'
	res225 = non_zeros(input_tif225)


	# In[322]:


	input_tif226 = '0226.TIF'
	res226 = non_zeros(input_tif226)


	# In[323]:


	input_tif227 = '0227.TIF'
	res227 = non_zeros(input_tif227)


	# In[324]:


	input_tif228 = '0228.TIF'
	res228 = non_zeros(input_tif228)


	# In[325]:


	input_tif229 = '0229.TIF'
	res229 = non_zeros(input_tif229)


	# In[326]:


	input_tif230 = '0230.TIF'
	res230 = non_zeros(input_tif230)


	# In[327]:


	input_tif231 = '0231.TIF'
	res231 = non_zeros(input_tif231)


	# In[328]:


	input_tif232 = '0232.TIF'
	res232 = non_zeros(input_tif232)


	# In[329]:


	input_tif233 = '0233.TIF'
	res233 = non_zeros(input_tif233)


	# In[330]:


	input_tif234 = '0234.TIF'
	res234 = non_zeros(input_tif234)


	# In[331]:


	input_tif235 = '0235.TIF'
	res235 = non_zeros(input_tif235)


	# In[332]:


	input_tif236 = '0236.TIF'
	res236 = non_zeros(input_tif236)


	# In[333]:


	input_tif237 = '0237.TIF'
	res237 = non_zeros(input_tif237)


	# In[334]:


	input_tif238 = '0238.TIF'
	res238 = non_zeros(input_tif238)


	# In[335]:


	input_tif239 = '0239.TIF'
	res239 = non_zeros(input_tif239)


	# In[336]:


	input_tif240 = '0240.TIF'
	res240 = non_zeros(input_tif240)


	# In[337]:


	input_tif241 = '0241.TIF'
	res241 = non_zeros(input_tif241)


	# In[338]:


	input_tif242 = '0242.TIF'
	res242 = non_zeros(input_tif242)


	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[ ]:





	# In[350]:



	final = pd.concat([res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13, res14, res15, res16, res17, res18, res19, res20, res21, res22, res23, res24, res25, res26, res27, res28, res29, res30, res31, res32, res33, res34, res35, res36, res37, res38, res39, res40, res41, res42, res43, res44, res45, res46, res47, res48, res49, res50, res51, res52, res53, res54, res55, res56, res57, res58, res59, res60, res61, res62, res63, res64, res65, res66, res67, res68, res69, res70, res71, res72, res73, res74, res75, res76, res77, res78, res79, res80, res81, res82, res83, res84, res85, res86, res87, res88, res89, res90, res91, res92, res93, res94, res95, res96, res97, res98, res99, res100, res101,res102,res103,res104,res105,res106,res107,res108, res109, res110, res111, res112, res113,res114,res115,res116,res117,res118,res119,res120,res121,res122,res123,res124,res125,res126,res127,res128,res129,res130,res131,res132,res133,res134,res135,res136,res137, res138,res139,res140,res141,res142,res143,res144,res145,res146,res147,res148,res149,res150,res151,res152,res153,res154,res155,res156,res157,res158,res159,res160,res161,res162,res163,res164,res165,res166,res167,res168,res169,res170,res171,res172,res173,res174,res175,res176,res177,res178,res179,res180,res181,res182,res183,res184,res185, res186, res187, res188, res189,res190, res191,res192, res193, res194, res195, res196, res197, res198, res199, res200, res201,res202, res203, res204, res205, res206, res207, res208, res209, res210, res211,res212,res213, res214, res215, res216, res217, res218, res219, res220,res221,res222,res223,res224,res225,res226,res227,res228,res229,res230,res231,res232,res233, res234, res235,res236, res237, res238,res239,res240,res241,res242
	                  ], axis=1)

	return final

