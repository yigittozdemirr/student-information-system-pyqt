import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from obs import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from obs import *
import sqlite3


#%% -----Uygulama----
class Sistem(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_OBS()
        self.ui.setupUi(self)
        
        global curs
        global conn
        db_path = os.path.join(BASE_DIR, "database", "veri.db")
        conn = sqlite3.connect(db_path)
        curs=conn.cursor()
        self.kontrol=False
        
        self.ui.cbbolum.addItem("Yazılım Mühendisliği", 1)
        self.ui.cbbolum.addItem("Makine Mühendisliği", 2)
        self.ui.cbbolum.addItem("Endüstri Mühendisliği", 3)
        self.ui.cbbolumgoster.addItem("Yazılım Mühendisliği", 1)
        self.ui.cbbolumgoster.addItem("Makine Mühendisliği", 2)
        self.ui.cbbolumgoster.addItem("Endüstri Mühendisliği", 3)
        
#%%----Sayfa Geçişleri------

        self.ui.btnana.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btnana2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btnana3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btnana4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.btnana5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        self.ui.btnana6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        
#%%----Bağlantı---
        self.ui.btngiriskayit.clicked.connect(self.KAYITEKRAN)
        self.ui.btngiriscikis.clicked.connect(self.CIKIS)
        self.ui.btnkayitcikis.clicked.connect(self.CIKIS)
        self.ui.btnkapa.clicked.connect(self.CIKIS)
        self.ui.btnkapa2.clicked.connect(self.CIKIS)
        self.ui.btnkapa3.clicked.connect(self.CIKIS)
        self.ui.btnkapa4.clicked.connect(self.CIKIS)
        self.ui.btnkapa5.clicked.connect(self.CIKIS)
        self.ui.btnkapa6.clicked.connect(self.CIKIS)
        self.ui.btngiris.clicked.connect(self.GIRIS)
        self.ui.btngirisdon.clicked.connect(self.GIRISDON)
        self.ui.btncikis.clicked.connect(self.OTURUM)
        self.ui.btncikis2.clicked.connect(self.OTURUM)
        self.ui.btncikis3.clicked.connect(self.OTURUM)
        self.ui.btncikis4.clicked.connect(self.OTURUM)
        self.ui.btncikis5.clicked.connect(self.OTURUM)
        self.ui.btncikis6.clicked.connect(self.OTURUM)
        self.ui.lnkayitsifre.textChanged.connect(self.SIFREC)
        self.ui.lnkayitsifretekrar.textChanged.connect(self.SIFREC)
        self.ui.btnkayit.clicked.connect(self.KAYIT)
        self.ui.btnobilgi.clicked.connect(self.BILGILER)
        self.ui.btnobilgi2.clicked.connect(self.BILGILER)
        self.ui.btnobilgi3.clicked.connect(self.BILGILER)
        self.ui.btnobilgi4.clicked.connect(self.BILGILER)
        self.ui.btnguncelle.clicked.connect(self.GUNCELLE)
        self.ui.btnsinif.clicked.connect(self.SINIF)
        self.ui.btnsinif2.clicked.connect(self.SINIF)
        self.ui.btnsinif3.clicked.connect(self.SINIF)
        self.ui.btnsinif4.clicked.connect(self.SINIF)
        self.ui.btnnotbilgi.clicked.connect(self.NOTLAR)
        self.ui.btnnotbilgi2.clicked.connect(self.NOTLAR)
        self.ui.btnnotbilgi3.clicked.connect(self.NOTLAR)
        self.ui.btnnotbilgi4.clicked.connect(self.NOTLAR)
        self.ui.btnduzen.clicked.connect(self.TUMTABLO)
        self.ui.btnduzen2.clicked.connect(self.TUMTABLO)
        self.ui.btnekle.clicked.connect(self.EKLE)
        self.ui.btnyeni.clicked.connect(self.YENI)
        self.ui.btnsil.clicked.connect(self.SIL)
        self.ui.lnara.textChanged.connect(self.ARA)
        self.ui.btnduzelt.clicked.connect(self.DUZELT)
        
#%%%---Girişe Dön---
    def GIRISDON(self):
        response=QMessageBox.question(self,"GİRİŞE DÖN","Girişe dönmek istediğinize emin misiniz?",\
                                            QMessageBox.Yes|QMessageBox.No)
        if response==QMessageBox.Yes:
            self.ui.lngirisid.clear()
            self.ui.lngirissifre.clear()
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lngirisid.setFocus()

#%%--DUZELTME TUŞU------

    def DUZELT(self):
        yeniid=self.ui.lnidgoster.text()
        ad=self.ui.lnadgoster.text() 
        soyad=self.ui.lnsoyadgoster.text()
        sifre=self.ui.lnsifregoster.text()
        bolum=self.ui.cbbolumgoster.currentData()
        vize1=self.ui.lnvizegoster1.text()
        vize2=self.ui.lnvizegoster2.text()
        vize3=self.ui.lnvizegoster3.text()
        final1=self.ui.lnfinalgoster1.text()
        final2=self.ui.lnfinalgoster2.text()
        final3=self.ui.lnfinalgoster3.text()
        liste=[yeniid,ad,soyad,sifre,vize1,vize2,vize3,final1,final2,final3]
          
        if not all(liste):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        
        try:
            vize1=int(vize1)
            vize2=int(vize2)
            vize3=int(vize3)
            final1=int(final1)
            final2=int(final2)
            final3=int(final3)
        except ValueError:
            QMessageBox.warning(self, "Uyarı", "Notlar sadece sayı olmalıdır!")
            return
        
        secilirow=self.ui.tableogretmen.currentRow()
        sec=self.ui.tableogretmen.item(secilirow,0)
        eskiid=sec.text()
        guncelle1="UPDATE ogrenciler SET ogrenciid=?, ogrenciad=?, ogrencisoyad=?, sifre=?, bolumid=? WHERE ogrenciid=?"
        curs.execute(guncelle1, (yeniid, ad, soyad, sifre, bolum, eskiid))
        conn.commit()

        guncelle2="UPDATE notlar SET vizenot1=?, vizenot2=?, vizenot3=?, finalnot1=?, finalnot2=?, finalnot3=?, ogrenciid=? WHERE ogrenciid=?"
        curs.execute(guncelle2, (vize1, vize2, vize3, final1, final2, final3, yeniid, eskiid))
        conn.commit()

        QMessageBox.information(self, "Başarılı", "Kayıt güncellendi.")
        
        curs.execute("""
                     SELECT 
                         o.ogrenciid,
                         o.ogrenciad,
                         o.ogrencisoyad,
                         b.bolumad,
                         o.sifre,
                         n.vizenot1,
                         n.vizenot2,
                         n.vizenot3,
                         n.finalnot1,
                         n.finalnot2,
                         n.finalnot3
                         FROM ogrenciler o
                         INNER JOIN bolumler b ON o.bolumid = b.bolumid
                         LEFT JOIN notlar n ON o.ogrenciid = n.ogrenciid
                         WHERE o.ogrenciid != '999'
                    """)
        result=curs.fetchall()
        rowcount=len(result)
        self.ui.tableogretmen.setRowCount(rowcount)
        currow=-1  

        for rowindex, rowdata in enumerate(result):
            for colindex, coldata in enumerate(rowdata):
                self.ui.tableogretmen.setItem(rowindex, colindex, QTableWidgetItem(str(coldata) if coldata is not None else ""))
        
            if str(rowdata[0])==yeniid:
                currow = rowindex

        if currow >= 0:
            self.ui.tableogretmen.setCurrentCell(currow, 0)
        elif rowcount > 0:
            self.ui.tableogretmen.setCurrentCell(0, 0)
            
#%%%-----ARA-----
    def ARA(self):
        ara=self.ui.lnara.text().strip()
        if not ara:
            curs.execute("""
                         SELECT 
                         o.ogrenciid,
                         o.ogrenciad,
                         o.ogrencisoyad,
                         b.bolumad,
                         o.sifre,
                         n.vizenot1,
                         n.vizenot2,
                         n.vizenot3,
                         n.finalnot1,
                         n.finalnot2,
                         n.finalnot3
                         FROM ogrenciler o
                         INNER JOIN bolumler b ON o.bolumid = b.bolumid
                         LEFT JOIN notlar n ON o.ogrenciid = n.ogrenciid
                         WHERE o.ogrenciid != '999'
                         """)
            result=curs.fetchall()
            rowcount=len(result)
            self.ui.tableogretmen.setRowCount(rowcount)
            
            for rowindex, rowdata in enumerate(result):
                for colindex, coldata in enumerate(rowdata):
                    self.ui.tableogretmen.setItem(rowindex, colindex, QTableWidgetItem(str(coldata) if coldata is not None else ""))
       
            if rowcount>0:
                self.ui.tableogretmen.setCurrentCell(0, 0)
            return
    
        aranacak = f"%{ara}%"
        arasql = """
            SELECT 
            o.ogrenciid, o.ogrenciad, o.ogrencisoyad, b.bolumad, o.sifre, 
            n.vizenot1, n.vizenot2, n.vizenot3, n.finalnot1, n.finalnot2, n.finalnot3
            FROM ogrenciler o
            INNER JOIN bolumler b ON o.bolumid = b.bolumid
            LEFT JOIN notlar n ON o.ogrenciid = n.ogrenciid
            WHERE o.ogrenciid != 999 AND (o.ogrenciad LIKE ? OR o.ogrencisoyad LIKE ?)
            """
        curs.execute(arasql, (aranacak, aranacak))
        result = curs.fetchall()
        rowcount = len(result)
        self.ui.tableogretmen.setRowCount(rowcount)
    
        for rowindex, rowdata in enumerate(result):
            for colindex, coldata in enumerate(rowdata):
                self.ui.tableogretmen.setItem(rowindex, colindex, QTableWidgetItem(str(coldata) if coldata is not None else ""))
    
        if rowcount>0:
            self.ui.tableogretmen.setCurrentCell(0, 0)

                
#%%-----SİL---------
    def SIL(self):
        response=QMessageBox.question(self,"Silme Onay","Seçili kaydı silmek istediğinize emin misin?",QMessageBox().Yes|QMessageBox().No)
        if response==QMessageBox.Yes:
            selectedrow=self.ui.tableogretmen.selectedItems()
            silinecek=selectedrow[0].text()
            deletesql="DELETE from ogrenciler where ogrenciid=?"
            parameter=[silinecek]
            curs.execute(deletesql,parameter)
            conn.commit()
            deletesql2="DELETE from notlar where ogrenciid=?"
            parameter2=[silinecek]
            curs.execute(deletesql2,parameter2)
            conn.commit()
            curs.execute("""
                         SELECT 
                         o.ogrenciid,
                         o.ogrenciad,
                         o.ogrencisoyad,
                         b.bolumad,
                         o.sifre,
                         n.vizenot1,
                         n.vizenot2,
                         n.vizenot3,
                         n.finalnot1,
                         n.finalnot2,
                         n.finalnot3
                         FROM ogrenciler o
                         INNER JOIN bolumler b ON o.bolumid = b.bolumid
                         LEFT JOIN notlar n ON o.ogrenciid = n.ogrenciid
                         WHERE o.ogrenciid != '999'
                         """)
            result=curs.fetchall()
            rowcount=len(result)
            self.ui.tableogretmen.setRowCount(rowcount)
            
            for rowindex, rowdata in enumerate(result):
                for colindex, coldata in enumerate(rowdata):
                    self.ui.tableogretmen.setItem(rowindex, colindex, QTableWidgetItem(str(coldata) if coldata is not None else ""))
       
            if rowcount>0:
                self.ui.tableogretmen.setCurrentCell(0, 0)
                QMessageBox().information(self,"Bilgilendirme","Kaydınız Silindi")

        
#%%-----YENİ--------
    def YENI(self):
        self.ui.lnidgoster.clear()
        self.ui.lnadgoster.clear()
        self.ui.lnsoyadgoster.clear()
        self.ui.lnsifregoster.clear()
        self.ui.lnvizegoster1.clear()
        self.ui.lnvizegoster2.clear()
        self.ui.lnvizegoster3.clear()
        self.ui.lnfinalgoster1.clear()
        self.ui.lnfinalgoster2.clear()
        self.ui.lnfinalgoster3.clear()
        self.ui.lnidgoster.setFocus()
   
#%%------EKLE TUŞU-----
    def EKLE(self):
        idno=self.ui.lnidgoster.text()
        ad=self.ui.lnadgoster.text() 
        soyad=self.ui.lnsoyadgoster.text()
        sifre=self.ui.lnsifregoster.text()
        bolum=self.ui.cbbolumgoster.currentData()
        vize1=self.ui.lnvizegoster1.text()
        vize2=self.ui.lnvizegoster2.text()
        vize3=self.ui.lnvizegoster3.text()
        final1=self.ui.lnfinalgoster1.text()
        final2=self.ui.lnfinalgoster2.text()
        final3=self.ui.lnfinalgoster3.text()
        liste=[idno,ad,soyad,sifre,vize1,vize2,vize3,final1,final2,final3]  
        
        if not all(liste):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        
        try:
            vize1=int(vize1)
            vize2=int(vize2)
            vize3=int(vize3)
            final1=int(final1)
            final2=int(final2)
            final3=int(final3)
        except ValueError:
            QMessageBox.warning(self, "Uyarı", "Notlar sadece sayı olmalıdır!")
            return
        
        
        curs.execute("SELECT * FROM ogrenciler WHERE ogrenciid = ?", (idno,))
        karsılastır=curs.fetchone()
        if karsılastır:
            QMessageBox.warning(self, "Uyarı", "Bu ID'ye sahip bir kullanıcı zaten var!")
            return
        
        insertsql="INSERT INTO ogrenciler (ogrenciid, ogrenciad, ogrencisoyad, sifre, bolumid) VALUES (?, ?, ?, ?, ?)"
        parameter=[idno, ad, soyad, sifre, bolum]
        curs.execute(insertsql, parameter)
        conn.commit()
        
        insertsql2="INSERT INTO notlar (ogrenciid, vizenot1, vizenot2, vizenot3, finalnot1, finalnot2, finalnot3) VALUES (?, ?, ?, ?, ?, ?, ?)"
        parameter2=[idno, vize1, vize2, vize3, final1, final2, final3]
        curs.execute(insertsql2, parameter2)
        conn.commit()        
        QMessageBox.information(self, "Başarılı", "Kayıt eklendi.")
        
        curs.execute("""
                     SELECT 
                         o.ogrenciid,
                         o.ogrenciad,
                         o.ogrencisoyad,
                         b.bolumad,
                         o.sifre,
                         n.vizenot1,
                         n.vizenot2,
                         n.vizenot3,
                         n.finalnot1,
                         n.finalnot2,
                         n.finalnot3
                         FROM ogrenciler o
                         INNER JOIN bolumler b ON o.bolumid = b.bolumid
                         LEFT JOIN notlar n ON o.ogrenciid = n.ogrenciid
                         WHERE o.ogrenciid != '999'
                    """)
        result=curs.fetchall()
        rowcount=len(result)
        self.ui.tableogretmen.setRowCount(rowcount) 
        currow=-1
        for rowindex, rowdata in enumerate(result):
            for colindex, coldata in enumerate(rowdata):
                self.ui.tableogretmen.setItem(rowindex, colindex, QTableWidgetItem(str(coldata) if coldata is not None else ""))
            if str(rowdata[0])==idno:
                currow=rowindex

        if currow>=0:
            self.ui.tableogretmen.setCurrentCell(currow, 0)
            
        else:
            if rowcount>0:
                self.ui.tableogretmen.setCurrentCell(0, 0)
        
        

#%%------TABLO TÜM BİLGİLER--------
    def TUMTABLO(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        curs.execute("""
                     SELECT 
                         o.ogrenciid,
                         o.ogrenciad,
                         o.ogrencisoyad,
                         b.bolumad,
                         o.sifre,
                         n.vizenot1,
                         n.vizenot2,
                         n.vizenot3,
                         n.finalnot1,
                         n.finalnot2,
                         n.finalnot3
                         FROM ogrenciler o
                         INNER JOIN bolumler b ON o.bolumid = b.bolumid
                         LEFT JOIN notlar n ON o.ogrenciid = n.ogrenciid
                         WHERE o.ogrenciid != '999'
                    """)
        result=curs.fetchall()
        rowcount=len(result)
        self.ui.tableogretmen.setRowCount(rowcount)      
        for rowindex, rowdata in enumerate(result):
            for colindex, coldata in enumerate(rowdata):
                self.ui.tableogretmen.setItem(rowindex, colindex, QTableWidgetItem(str(coldata) if coldata is not None else ""))
        if rowcount>0:
            self.ui.tableogretmen.setCurrentCell(0, 0)
            
        selectedrows=self.ui.tableogretmen.selectedItems() 
        if selectedrows:
            self.ui.lnidgoster.setText(selectedrows[0].text())
            self.ui.lnadgoster.setText(selectedrows[1].text()) 
            self.ui.lnsoyadgoster.setText(selectedrows[2].text())
            
            bolum=selectedrows[3].text()
            index=self.ui.cbbolumgoster.findText(bolum)
            if index >= 0:
                self.ui.cbbolumgoster.setCurrentIndex(index)
                
            self.ui.lnsifregoster.setText(selectedrows[4].text())
            self.ui.lnvizegoster1.setText(selectedrows[5].text())
            self.ui.lnvizegoster2.setText(selectedrows[6].text())
            self.ui.lnvizegoster3.setText(selectedrows[7].text())
            self.ui.lnfinalgoster1.setText(selectedrows[8].text())
            self.ui.lnfinalgoster2.setText(selectedrows[9].text())
            self.ui.lnfinalgoster3.setText(selectedrows[10].text())
        self.ui.tableogretmen.cellClicked.connect(self.DOLDUR)
            
#%%%--DOLDUR----
    def DOLDUR(self):            
        selectedrows=self.ui.tableogretmen.selectedItems() 
        if selectedrows:
            self.ui.lnidgoster.setText(selectedrows[0].text())
            self.ui.lnadgoster.setText(selectedrows[1].text()) 
            self.ui.lnsoyadgoster.setText(selectedrows[2].text())
            
            bolum=selectedrows[3].text()
            index=self.ui.cbbolumgoster.findText(bolum)
            if index>=0:
                self.ui.cbbolumgoster.setCurrentIndex(index)
                
            self.ui.lnsifregoster.setText(selectedrows[4].text())
            self.ui.lnvizegoster1.setText(selectedrows[5].text())
            self.ui.lnvizegoster2.setText(selectedrows[6].text())
            self.ui.lnvizegoster3.setText(selectedrows[7].text())
            self.ui.lnfinalgoster1.setText(selectedrows[8].text())
            self.ui.lnfinalgoster2.setText(selectedrows[9].text())
            self.ui.lnfinalgoster3.setText(selectedrows[10].text())
        
        
        
#%%------Not Bilgileri--------
    def NOTLAR(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        girisid2=self.ui.lngirisid.text()
        girissifre2=self.ui.lngirissifre.text()
        curs.execute("SELECT bolumid FROM ogrenciler WHERE ogrenciid = ? AND sifre = ?", (girisid2, girissifre2))
        bolumsonuc2=curs.fetchone()
        if bolumsonuc2:
            bolumid2=bolumsonuc2[0]
            curs.execute("SELECT dersad FROM dersler WHERE bolumid = ?", (bolumid2,))
            result2=curs.fetchall()  
            ders1=result2[0][0]
            ders2=result2[1][0]
            ders3=result2[2][0]
            self.ui.lnders1.setText(ders1)
            self.ui.lnders2.setText(ders2)
            self.ui.lnders3.setText(ders3)
            
        curs.execute("SELECT vizenot1, vizenot2, vizenot3, finalnot1, finalnot2, finalnot3 FROM notlar WHERE ogrenciid=?", (girisid2,))
        notlar=curs.fetchone()
        if notlar:    
            not1, not2, not3, not4, not5, not6 = notlar
            self.ui.lnvizenot.setText(f"Vize: {not1 if not1 is not None else ''}")
            self.ui.lnvizenot2.setText(f"Vize: {not2 if not2 is not None else ''}")
            self.ui.lnvizenot3.setText(f"Vize: {not3 if not3 is not None else ''}")
            self.ui.lnfinalnot.setText(f"Final: {not4 if not4 is not None else ''}")
            self.ui.lnfinalnot2.setText(f"Final: {not5 if not5 is not None else ''}")
            self.ui.lnfinalnot3.setText(f"Final: {not6 if not6 is not None else ''}")
            
            if notlar and None not in notlar:             
                hesap1=(float(not1)*0.4)+(float(not4)*0.6)
                hesap2=(float(not2)*0.4)+(float(not5)*0.6)
                hesap3=(float(not3)*0.4)+(float(not6)*0.6)
                sonhesap=(hesap1+hesap2+hesap3)/3
                hesapdortluk=(sonhesap/100)*4
                self.ui.lblort.setText(f"{sonhesap:.2f} -> {hesapdortluk:.2f}")
            
            else:
                self.ui.lblort.setText("Henüz notlar girilmemiş")
                
            
        
#%%-----Bilgiler-----
    def BILGILER(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        if self.kontrol:
            girisid=self.ui.lngirisid.text()
            girissifre=self.ui.lngirissifre.text()
        
            curs.execute("SELECT ogrenciad, ogrencisoyad, ogrenciid, sifre, bolumid FROM ogrenciler WHERE ogrenciid = ? AND sifre = ?", (girisid, girissifre))
            bilgiler=curs.fetchone()
        
            bilgiad,bilgisoyad,bilgiid,bilgisifre,bilgibolum=bilgiler
            self.ui.lnad.setText(f"{bilgiad}")
            self.ui.lnsoyad.setText(f"{bilgisoyad}")
            self.ui.lnid.setText(f"{bilgiid}")
            index=self.ui.cbbolum.findData(bilgibolum)
            bolumad=self.ui.cbbolum.itemText(index)
            self.ui.lnbolum.setText(f"{bolumad}")
            self.ui.lnsifre.setText(f"{bilgisifre}")
        
#%%-----Sınıf Bilgi----
    def SINIF(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        girisid=self.ui.lngirisid.text()
        girissifre=self.ui.lngirissifre.text()
        curs.execute("SELECT bolumid FROM ogrenciler WHERE ogrenciid = ? AND sifre = ? ", (girisid, girissifre))
        bolumsonuc=curs.fetchone()

        if bolumsonuc:
            bolumid=bolumsonuc[0]
            index=self.ui.cbbolum.findData(bolumid)
            bolumad=self.ui.cbbolum.itemText(index)
            self.ui.lbsinif.setText(f"{bolumad} Sınıfı")
            curs.execute("SELECT ogrenciid, ogrenciad, ogrencisoyad FROM ogrenciler WHERE bolumid = ? AND ogrenciid != '999'", (bolumid,))
            result=curs.fetchall()
            rowcount=len(result)
            self.ui.lblmevcut.setText(str(rowcount))
            self.ui.tablesinif.setRowCount(rowcount)
            
            if rowcount>0:
                self.ui.tablesinif.setCurrentCell(0, 0)

            for rowindex, rowdata in enumerate(result):
                for colindex, coldata in enumerate(rowdata):
                    self.ui.tablesinif.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))

        
                
        
#%%-----Bilgileri Güncelle-----
    def GUNCELLE(self):
        ad=self.ui.lnad.text()
        soyad=self.ui.lnsoyad.text()
        sifre2=self.ui.lnsifre.text()
        idno=self.ui.lngirisid.text()  
        liste2=[ad, soyad, sifre2]

        if not all(liste2):
            QMessageBox.warning(self, "Eksik Bilgi", "Tüm alanları doldurun.")
            return

        curs.execute("UPDATE ogrenciler SET ogrenciad = ?, ogrencisoyad = ?, sifre = ? WHERE ogrenciid = ?", (ad, soyad, sifre2, idno))
        conn.commit()
        QMessageBox.information(self, "Başarılı", "Bilgiler güncellendi.")

        curs.execute("SELECT ogrenciid, ogrenciad, ogrencisoyad FROM ogrenciler WHERE ogrenciid=?", (idno,))
        sonuc2 = curs.fetchone()
        if sonuc2:
            numara2, ad2, soyad2 = sonuc2
            bilgitext = f"{numara2} - {ad2} {soyad2}"
            self.ui.lbbilgi.setText(bilgitext)
            self.ui.lbbilgi2.setText(bilgitext)
            self.ui.lbbilgi3.setText(bilgitext)
            self.ui.lbbilgi4.setText(bilgitext)

        curs.execute("SELECT bolumid FROM ogrenciler WHERE ogrenciid = ?", (idno,))
        bolumsonuc = curs.fetchone()

        if bolumsonuc:
            bolumid = bolumsonuc[0]
            index = self.ui.cbbolum.findData(bolumid)
            bolumad = self.ui.cbbolum.itemText(index)
            self.ui.lbsinif.setText(f"{bolumad} Sınıfı")

            curs.execute("SELECT ogrenciid, ogrenciad, ogrencisoyad FROM ogrenciler WHERE bolumid = ? AND ogrenciid != '999'", (bolumid,))
            result = curs.fetchall()

            self.ui.tablesinif.clearContents()
            self.ui.tablesinif.setRowCount(0)

            rowcount = len(result)
            self.ui.lblmevcut.setText(str(rowcount))
            self.ui.tablesinif.setRowCount(rowcount)

            if rowcount>0:
                self.ui.tablesinif.setCurrentCell(0, 0)
                
            for rowindex, rowdata in enumerate(result):
                for colindex, coldata in enumerate(rowdata):
                    self.ui.tablesinif.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))   
                    
#%%------Giriş-------

    def GIRIS(self):
        kullaniciid = self.ui.lngirisid.text()
        kullanicisifre = self.ui.lngirissifre.text()

        if not kullaniciid or not kullanicisifre:
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen kullanıcı ID ve şifre girin.")
            return
            
        curs.execute("SELECT ogrenciid, ogrenciad, ogrencisoyad FROM ogrenciler WHERE ogrenciid = ? AND sifre = ?", (kullaniciid, kullanicisifre))
        sonuc = curs.fetchone()
        
        if sonuc:
            numara,ad,soyad=sonuc
            if kullaniciid=="999":
                self.ui.lbbilgi5.setText("Yönetici - Yiğit Özdemir")
                self.ui.lbbilgi6.setText("Yönetici - Yiğit Özdemir")
                QMessageBox.information(self, "Giriş Başarılı", f"Hoş geldin {ad} {soyad}!")
                self.ui.stackedWidget.setCurrentIndex(6)
                
            else:
                self.ui.lbbilgi.setText(f"{numara} - {ad} {soyad}")
                self.ui.lbbilgi2.setText(f"{numara} - {ad} {soyad}")
                self.ui.lbbilgi3.setText(f"{numara} - {ad} {soyad}")
                self.ui.lbbilgi4.setText(f"{numara} - {ad} {soyad}")
                QMessageBox.information(self, "Giriş Başarılı", f"Hoş geldin {ad} {soyad}!")
                self.ui.stackedWidget.setCurrentIndex(2)                
            self.kontrol=True
            
        else:
            self.kontrol=False
            QMessageBox.warning(self, "Hatalı Giriş", "Kullanıcı ID veya şifre hatalı!")
            
#%%---Şifre Kontrol----
    def SIFREC(self):
        sifre=self.ui.lnkayitsifre.text()
        sifre2=self.ui.lnkayitsifretekrar.text()
        
        if sifre!=sifre2:
            self.ui.lbsifre.setText("❌ Şifreler uyuşmuyor!")
            self.ui.lbsifre.setStyleSheet("color: red; font-weight: bold;")
        
        else:
            self.ui.lbsifre.setText("✅ Şifreler uyuşuyor.")
            self.ui.lbsifre.setStyleSheet("color: green; font-weight: bold;")        
#%%----Kayıt ekranı----
    def KAYITEKRAN(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.lnkayitid.clear()
        self.ui.lnkayitad.clear()
        self.ui.lnkayitsoyad.clear()
        self.ui.lnkayitsifre.clear()
        self.ui.lnkayitsifretekrar.clear()
        self.ui.lnkayitid.setFocus()    

#%%----Kayıt----
    def KAYIT(self):
        
        _ogrenciid=self.ui.lnkayitid.text()
        _ogrenciad=self.ui.lnkayitad.text()
        _ogrencisoyad=self.ui.lnkayitsoyad.text()
        _sifre=self.ui.lnkayitsifre.text()
        _bolumid=self.ui.cbbolum.currentData()
        _sifretekrar=self.ui.lnkayitsifretekrar.text()
        liste=[_ogrenciid, _ogrenciad, _ogrencisoyad, _sifre, _bolumid, _sifretekrar]
        
        
        if not all(liste):
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        
        if _sifre!=_sifretekrar:
            QMessageBox.warning(self, "Uyarı", "Şifreler uyuşmuyor!")
            return
        
        curs.execute("SELECT * FROM ogrenciler WHERE ogrenciid = ?", (_ogrenciid,))
        karsılastır=curs.fetchone()
        if karsılastır:
            QMessageBox.warning(self, "Uyarı", "Bu ID'ye sahip bir kullanıcı zaten var!")
            return
        
        insertsql = "INSERT INTO ogrenciler (ogrenciid, ogrenciad, ogrencisoyad, sifre, bolumid) VALUES (?, ?, ?, ?, ?)"
        parameter= [_ogrenciid, _ogrenciad, _ogrencisoyad, _sifre, _bolumid]
        curs.execute(insertsql, parameter)
        conn.commit()
        insertsql2 = "INSERT INTO notlar (ogrenciid) VALUES (?)"
        parameter2= [_ogrenciid]
        curs.execute(insertsql2, parameter2)
        conn.commit()
        
        QMessageBox.information(self, "Başarılı", "Kayıt eklendi.")
        self.ui.stackedWidget.setCurrentIndex(0)


#%%---Oturum Kapa-----
    def OTURUM(self):
        response=QMessageBox.question(self,"OTURUM","Oturumu kapatmak istediğinize emin misiniz?",\
                                            QMessageBox.Yes|QMessageBox.No)
        if response==QMessageBox.Yes:
            self.ui.lngirisid.clear()
            self.ui.lngirissifre.clear()
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lngirisid.setFocus()
            
        
#%%----Çıkış----
    def CIKIS(self):
        response=QMessageBox.question(self,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                                        QMessageBox.Yes|QMessageBox.No)
        if response==QMessageBox.Yes:
            conn.close()
            self.close()          
#%%------Çalıştır---------
if __name__=="__main__":
    app=QApplication(sys.argv) 
    pencere=Sistem()  
    pencere.show() 
    sys.exit(app.exec_())

#%%



        