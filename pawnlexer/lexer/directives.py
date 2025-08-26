tokens = (
    'LOCAL_INCLUDE',
    'GLOBAL_INCLUDE',
    'PRAGMA',
    'DEFINE'
)


def t_LOCAL_INCLUDE(t):
    r'\#include\s+[\""][a-zA-Z0-9_\/\.-]+[\""]'
    t.value = t.value[1:-1]
    return t


def t_GLOBAL_INCLUDE(t):
    r'\#include\s+[<"][a-zA-Z0-9_\/\.-]+[>"]'
    t.value = t.value[1:-1]
    return t


def t_PRAGMA(t):
    r'\#pragma'
    return t


def t_DEFINE(t):
    r'\#define'
    return t