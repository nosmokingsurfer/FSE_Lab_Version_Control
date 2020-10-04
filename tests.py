from storage import Storage

def test_add():
    pass

def test_remove():

    try:
        print("Trying to remove")
        data = {"one": 1, "two": 2}
        test = Storage(data)
        test.remove("one")
    except KeyError as e:
        print(e)
        print("Remove function failed with data:", data)
    else:
        print("OK")

    
    try:
        print("Trying to remove twice...")
        data = {"one" : 1, "two" : 2}
        test.remove("one")
        test.remove("one")
    except KeyError as e:
        print("OK")
    else:
        print("Not OK")
        print("Failed on data:", data)

    pass

def test_set():
    pass

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    #test_add()
    test_remove()
    #test_set()
    test_get()

if __name__ == "__main__":
    run_tests()