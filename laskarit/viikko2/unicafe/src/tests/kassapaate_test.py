import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_luotu_kassa_oikein(self):
        self.assertEqual(round(self.kassa.kassassa_rahaa / 100, 2), 1000)
        self.assertEqual(self.kassa.edulliset+self.kassa.maukkaat, 0)

    def test_kateisosto_toimii_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(round(self.kassa.kassassa_rahaa / 100, 2), 1002.4)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230), 230)

    def test_kateisosto_toimii_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(410)
        self.kassa.syo_maukkaasti_kateisella(230)
        self.assertEqual(round(self.kassa.kassassa_rahaa / 100, 2), 1004.0)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(230), 230)

    def test_korttiosto_toimii_edullinen(self):
        kortti = Maksukortti(440)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(kortti.saldo, 200)
        kortti = Maksukortti(400)
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(kortti))
        self.assertEqual(round(self.kassa.kassassa_rahaa / 100, 2), 1000)
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 2)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(kortti))

    def test_korttiosto_toimii_maukas(self):
        kortti = Maksukortti(440)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(kortti.saldo, 40)
        kortti = Maksukortti(400)
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(round(self.kassa.kassassa_rahaa / 100, 2), 1000)
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.maukkaat, 2)
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(kortti))
    
    def test_lataaminen_toimii_kassalla(self):
        kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(round(self.kassa.kassassa_rahaa / 100, 2), 1001.0)
        self.assertIsNone(self.kassa.lataa_rahaa_kortille(kortti, -100))
