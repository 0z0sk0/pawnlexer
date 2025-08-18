tokens = (
    'INCLUDE',
    'LOCAL_INCLUDE_PATH',
    'GLOBAL_INCLUDE_PATH',
    'PRAGMA',
    'DEFINE'
)


def t_INCLUDE(t):
    r'\#include'
    return t


def t_LOCAL_INCLUDE_PATH(t):
    r'[\""][a-zA-Z0-9_\/\.-]+[\""]'
    t.value = t.value[1:-1]
    return t


def t_GLOBAL_INCLUDE_PATH(t):
    r'[<"][a-zA-Z0-9_\/\.-]+[>"]'
    t.value = t.value[1:-1]
    return t


def t_PRAGMA(t):
    r'\#pragma'
    return t


def t_DEFINE(t):
    r'\#define'
    return t