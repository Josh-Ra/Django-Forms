from django.test import TestCase


# Create your tests here.
class TestWarmup2(TestCase):
    def test1(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&number=3")
        self.assertContains(response, "ChoChoCho")

    def test2(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&number=2")
        self.assertContains(response, "ChoCho")

    def test3(self):
        response = self.client.get("/warmup-2/font-times/?word=Abc&number=3")
        self.assertContains(response, "AbcAbcAbc")


class TestLogic2(TestCase):
    def test1(self):
        response = self.client.get("/logic-2/no-teen-sum/?number1=1&number2=2&number3=3")
        self.assertContains(response, 6)

    def test2(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/?number1=2&number2=1&number3=13"
        )
        self.assertContains(response, 3)

    def test3(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/?number1=2&number2=1&number3=14"
        )
        self.assertContains(response, 3)


class TestString2(TestCase):
    def test1(self):
        response = self.client.get("/string-2/xyz-there/?word=abcxyz")
        self.assertContains(response, True)

    def test2(self):
        response = self.client.get("/string-2/xyz-there/?word=abc.xyz")
        self.assertContains(response, False)

    def test3(self):
        response = self.client.get("/string-2/xyz-there/?word=xyz.abc")
        self.assertContains(response, True)


class TestList2(TestCase):
    def test1(self):
        response = self.client.get(
            "/list-2/centered-average/?Number0=1&Number1=2&Number2=3&Number3=4&Number4=100&Number5=&Number6="
        )
        self.assertContains(response, 3)

    def test2(self):
        response = self.client.get(
            "/list-2/centered-average/?Number0=1&Number1=1&Number2=5&Number3=5&Number4=10&Number5=7&Number6=8"
        )
        self.assertContains(response, 5)

    def test3(self):
        response = self.client.get(
            "/list-2/centered-average/?Number0=-10&Number1=-4&Number2=-2&Number3=-4&Number4=-2&Number5=0&Number6="
        )
        self.assertContains(response, -3)
