def pytest_generate_tests(metafunc):
    '''
    Точка входа pytest: вызывается для параметризации теста
    '''
    if metafunc.cls is None:
        return

    mro_list = metafunc.cls.mro()