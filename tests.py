from storage import Storage

def test_add(): #Катя
    st = Storage({'a': 1, 'b': 2})
    key = 'ItsAKEy'
    value = 'ItsAValue'
    
    st.add(key, value)
    assert st.data[key] == value, "The key {} is absent or value is not equal to expected one {}".format(key, value)
    print(st)


def test_remove():
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
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
