import sys

import loader_dat
import loader_map
import loader_frm
import loader_pal
import loader_fon
import loader_aaf

#urlprefix = "../data/"	# use this to point to the directory with the undat'd Fallout2 data
urlprefix = ""	# use this to point to the directory with the undat'd Fallout2 data

loadData = {}
		

	
def loadGameState(loadVars):

	master_dat_file = "".join([urlprefix,"master.dat"])
	master_dat = loader_dat.loadDAT(master_dat_file)

	critter_dat_file = "".join([urlprefix,"critter.dat"])
	critter_dat = loader_dat.loadDAT(critter_dat_file)
	
	color = loader_pal.loadPAL(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["color.pal"]))
	
	def loadFRM(datname, datfile, filename):		#these functions look hideous, I'll fix this one day
		if(filename not in datfile["fileEntries"]):
			return
	
		if(filename not in loadData):
			loadItem =  loader_frm.loadFRM(loader_dat.getFile(datname,datfile["fileEntries"][filename]),color)
			if(loadItem is not None):
				loadData[filename] = loadItem


	def loadCritter(frmindex):
		loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"aa.frm"]))
		loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ab.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ae.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ag.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ah.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ai.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"aj.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ak.frm"]))
		loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"al.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"an.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ao.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ap.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"aq.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ar.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"as.frm"]))
		loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"at.frm"]))


		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ba.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bb.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bc.frm"]))
		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.fr0"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.fr1"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.fr2"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.fr3"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.fr4"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bd.fr5"]))			
		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"be.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bf.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bg.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bh.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bi.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bj.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bk.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bl.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bm.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bn.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bo.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"bp.frm"]))
		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ch.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"cj.frm"]))
		
		for r in range(9):	# D-M
			loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 3 + r) + "a.frm"]))
			loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 3 + r) + "b.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 3 + r) + "c.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 3 + r) + "d.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 3 + r) + "e.frm"]))
		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"df.frm"]))
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ef.frm"]))		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"ff.frm"]))		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"gf.frm"]))
		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"dg.frm"]))	
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"eg.frm"]))		
		#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,"fg.frm"]))

		#for r in range(5):
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 7 + r) + "h.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 7 + r) + "i.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 7 + r) + "j.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 7 + r) + "k.frm"]))
			#loadFRM(critter_dat_file,critter_dat,"".join(["art/critters/",frmindex,chr(97 + 7 + r) + "l.frm"]))	

	
	
	mapIndex = "".join( ['maps/', loadVars['map'] ] )
	loadData[mapIndex] = loader_map.loadMAP("".join([urlprefix,mapIndex]) )
	
	loadData["font0.aaf"] = loader_aaf.loadAAF(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font0.aaf"]))	# fonts
	loadData["font1.aaf"] = loader_aaf.loadAAF(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font1.aaf"]))	# fonts
	loadData["font2.aaf"] = loader_aaf.loadAAF(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font2.aaf"]))	# fonts
	loadData["font3.aaf"] = loader_aaf.loadAAF(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font3.aaf"]))	# fonts
	loadData["font4.aaf"] = loader_aaf.loadAAF(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font4.aaf"]))	# fonts

	
	loadData["font0.fon"] = loader_fon.loadFON(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font0.fon"]))	# fonts
	loadData["font0.fon"] = loader_fon.loadFON(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font1.fon"]))	# fonts
	loadData["font0.fon"] = loader_fon.loadFON(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font2.fon"]))	# fonts
	loadData["font0.fon"] = loader_fon.loadFON(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font3.fon"]))	# fonts
	loadData["font0.fon"] = loader_fon.loadFON(loader_dat.getFile(master_dat_file, master_dat["fileEntries"]["font5.fon"]))	# fonts

	msgFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["text/english/game/pro_crit.msg"])
	loadData["text/english/game/pro_crit.msg"] = {}
	loadData["text/english/game/pro_crit.msg"]["data"] = []
	for line in msgFile:
		loadData["text/english/game/pro_crit.msg"]["data"].append(line.decode("utf-8").strip().lower())	
	
	msgFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["text/english/game/pro_item.msg"])
	loadData["text/english/game/pro_item.msg"] = {}
	loadData["text/english/game/pro_item.msg"]["data"] = []
	for line in msgFile:
		loadData["text/english/game/pro_item.msg"]["data"].append(line.decode("utf-8").strip().lower())	
	
	msgFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["text/english/game/pro_scen.msg"])
	loadData["text/english/game/pro_scen.msg"] = {}
	loadData["text/english/game/pro_scen.msg"]["data"] = []
	for line in msgFile:
		loadData["text/english/game/pro_scen.msg"]["data"].append(line.decode("utf-8").strip().lower())	

	msgFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["text/english/game/pro_misc.msg"])
	loadData["text/english/game/pro_misc.msg"] = {}
	loadData["text/english/game/pro_misc.msg"]["data"] = []
	for line in msgFile:
		loadData["text/english/game/pro_misc.msg"]["data"].append(line.decode("utf-8").strip().lower())	

	msgFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["text/english/game/pro_wall.msg"])
	loadData["text/english/game/pro_wall.msg"] = {}
	loadData["text/english/game/pro_wall.msg"]["data"] = []
	for line in msgFile:
		loadData["text/english/game/pro_wall.msg"]["data"].append(line.decode("utf-8").strip().lower())	

	msgFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["text/english/game/pro_tile.msg"])
	loadData["text/english/game/pro_tile.msg"] = {}
	loadData["text/english/game/pro_tile.msg"]["data"] = []
	for line in msgFile:
		loadData["text/english/game/pro_tile.msg"]["data"].append(line.decode("utf-8").strip().lower())	


	lstFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["art/items/items.lst"])
	loadData["art/items/items.lst"] = []
	for line in lstFile:
		loadData["art/items/items.lst"].append(line.decode("utf-8").strip().lower())

	lstFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["art/walls/walls.lst"])
	loadData["art/walls/walls.lst"] = []
	for line in lstFile:
		loadData["art/walls/walls.lst"].append(line.decode("utf-8").strip().lower())

	lstFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["art/tiles/tiles.lst"])
	loadData["art/tiles/tiles.lst"] = []
	for line in lstFile:
		loadData["art/tiles/tiles.lst"].append(line.decode("utf-8").strip().lower())

	lstFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["art/scenery/scenery.lst"])	
	loadData["art/scenery/scenery.lst"] = []
	for line in lstFile:
		loadData["art/scenery/scenery.lst"].append(line.decode("utf-8").strip().lower())

	lstFile = loader_dat.getFile(master_dat_file,master_dat["fileEntries"]["art/misc/misc.lst"])	
	loadData["art/misc/misc.lst"] = []
	for line in lstFile:
		loadData["art/misc/misc.lst"].append(line.decode("utf-8").strip().lower())
		
	lstFile = loader_dat.getFile(critter_dat_file,critter_dat["fileEntries"]["art/critters/critters.lst"])	
	loadData["art/critters/critters.lst"] = []
	for line in lstFile:
		line = line.decode("utf-8").strip().lower()
		split = line.split(',')
		
		if(len(split) > 1):
			critter = {}
			critter['base'] = split[0]
			critter['ID1'] = split[1]
			if(len(split) > 2):
				critter['ID2'] = split[2]
		else:
			critter = line
		
		loadData["art/critters/critters.lst"].append(critter)


	loadFRM(master_dat_file,master_dat,"art/intrface/msef000.frm")		#hex cursors
	loadFRM(master_dat_file,master_dat,"art/intrface/msef003.frm")
	
	loadFRM(master_dat_file,master_dat,"art/intrface/screast.frm")		#scroll cursors
	loadFRM(master_dat_file,master_dat,"art/intrface/screx.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrneast.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrnex.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrnorth.frm")
	
	loadFRM(master_dat_file,master_dat,"art/intrface/scrnwest.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrnwx.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrseast.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrnx.frm")
	
	loadFRM(master_dat_file,master_dat,"art/intrface/scrsex.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrsouth.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrswest.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrswx.frm")
	
	loadFRM(master_dat_file,master_dat,"art/intrface/scrsx.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrwest.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/scrwx.frm")
	
	
	loadFRM(master_dat_file,master_dat,"art/intrface/actarrow.frm")
	
	loadFRM(master_dat_file,master_dat,"art/intrface/iface.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/stdarrow.frm")

	
	loadFRM(master_dat_file,master_dat,"art/intrface/usegetn.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/usegeth.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/talkn.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/talkh.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/skilln.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/skillh.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/rotaten.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/rotateh.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/pushn.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/pushh.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/lookn.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/lookh.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/invenn.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/invenh.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/canceln.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/cancelh.frm")
		
	loadFRM(master_dat_file,master_dat,"art/intrface/opbase.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/opbtnoff.frm")
	loadFRM(master_dat_file,master_dat,"art/intrface/opbtnon.frm")

		
	loadCritter("hmjmps")
	
		
	def getFiletype(typeID):
		if(typeID == 0):
			return "items"
		elif(typeID == 1):
			return "critters"
		elif(typeID == 2):
			return "scenery"
		elif(typeID == 3):
			return "walls"
		elif(typeID == 4):
			return "tiles"
		elif(typeID == 5):
			return "misc"
	
	
	for e in range(loadData[mapIndex]['nElevations']):		# load tile FRM
		for i in range(10000):
			index = loadData[mapIndex]['tileInfo'][e]['floorTiles'][i]
			filename = "".join(["art/tiles/", loadData['art/tiles/tiles.lst'][index] ]).lower()
		
			loadFRM(master_dat_file,master_dat,filename)

			index = loadData[mapIndex]['tileInfo'][e]['roofTiles'][i]
			filename = "".join(["art/tiles/", loadData['art/tiles/tiles.lst'][index] ]).lower()
		
			loadFRM(master_dat_file,master_dat,filename)
	

		for i in range(len(loadData[mapIndex]['objectInfo'][e])):
			index = loadData[mapIndex]['objectInfo'][e][i]['frmID']
			filetype = getFiletype(loadData[mapIndex]['objectInfo'][e][i]['frmTypeID'])
			
			if(filetype == "critters"):
				loadCritter(loadData['art/critters/critters.lst'][index]['base'])
			else:	
				lstname = "".join(["art/",filetype,"/",filetype,".lst"])
				filename = "".join(["art/",filetype,"/", loadData[lstname][index] ]).lower()
				loadFRM(master_dat_file,master_dat,filename)
			
			for k in range(loadData[mapIndex]['objectInfo'][e][i]['inventorySize']):
				invfiletype = getFiletype(loadData[mapIndex]['objectInfo'][e][i]['inventory'][k]['frmTypeID'])
				invindex = loadData[mapIndex]['objectInfo'][e][i]['inventory'][k]['frmID']
				
				if(invfiletype == "critters"):
					loadCritter(loadData['art/critters/critters.lst'][invindex]['base'])
				else:
					lstname = "".join(["art/",invfiletype,"/",invfiletype,".lst"])
					filename = "".join(["art/",invfiletype,"/", loadData[lstname][invindex] ]).lower()
					loadFRM(master_dat_file,master_dat,filename)
			
			
	return loadData