try:
    from run import app
    import unittest

except Exception as e:
    print("Some Modules are Missing{}".format(e))

class FlaskTeat(unittest.TestCase):

    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertEqual(response.content_type, "application/json")

if __name__ == "__main__":
    unittest.main()
