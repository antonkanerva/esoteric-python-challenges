#!/usr/bin/env python3.6
"""
    Submission by amp180.
"""
import string
import random

ZERO = int()
ONE = len([None,])
TWO = ONE + ONE
TEN = (ONE << (TWO + ONE)) + (TWO)
_ = string.punctuation[-(TWO + TWO + TWO)]
SPACE = string.whitespace[ZERO]


class ReprMixin():
    def __repr__(self):
        words = str()
        for k in self.__class__.__dict__.keys():
            if _ not in k:
                words += (k.strip() + SPACE)
        return words


class EnterShikari_RabbleRouser_2017(ReprMixin):
    I = ...
    torture = ...
    rock = ...
    stars = ...
    With = ...
    pliers = ...

    Theyre = ...
    so = ...
    stock = ...
    it = ...
    wouldnt = ...
    be = ...
    a = ...
    shock = ...
    
    If = ...
    I = ...
    Open = ...
    them = ...
    up = ...
    to = ...
    see = ...
    wires = ...

    I = ...
    destroy = ...
    All = ...
    amplifiers = ...

    People = ...
    climbing = ...
    over = ...
    bodies = ...
    like = ...
    spiders = ...

    Im = ...
    on = ...
    stage = ...
    With = ...
    a = ...
    face = ...
    like = ...
    a = ...
    sack = ...
    of = ...
    screwdrivers = ...

    And = ...
    its = ...
    gonna = ...
    be = ...
    a = ...
    show = ...
    stop = ...
    road = ...
    block = ...

    And = ...
    we = ...
    are = ...
    the = ...
    epicentre = ...
    of = ...
    the = ...
    bedrock = ...
    of = ...
    a = ...
    new = ...
    sound = ...

    I = ...
    say = ...
    were = ...
    coming = ...
    For = ...
    you = ...
    And = ...

    I = ...
    say = ...
    it = ...
    With = ...
    face = ...
    like = ...
    a = ...
    sack = ...
    of = ...
    screw = ...
    screw = ...
    screw = ...
    screw = ...

    Whats = ...
    your = ...
    criteria = ...

    Complete = ...
    hysteria = ...

    Decibels = ...
    so = ...
    Max = ...
    you = ...
    can = ...
    yell = ...
    out = ...
    your = ...
    deep = ...
    secrets = ...

    Nobodys = ...
    gonna = ...
    hear = ...
    you = ...

    Whats = ...
    your = ...
    medium = ...

    Complete = ...
    delirium = ...

    The = ...
    lunatics = ...
    took = ...
    over = ...
    the = ...
    asylum = ...

    En = ...
    garde = ...

    warning = ...
    this = ...
    escalates = ...
    quickly = ...

    Are = ...
    you = ...
    getting = ...
    nervous = ...

    Are = ...
    you = ...
    getting = ...
    nervous = ...

    The = ...
    mist = ...
    rolls = ...
    In = ...
    thickly = ...

    Are = ...
    you = ...
    getting = ...
    nervous = ...

    Have = ...
    you = ...
    lost = ...
    your = ...
    nerve = ...

    Whats = ...
    your = ...
    technique = ...

    So = ...
    so = ...
    so = ...
    so = ...
    unique = ...

    Fuck = ...
    ego = ...
    minimise = ...
    the = ...
    self = ...
    Maximise = ...
    the = ...
    bond = ...
    the = ...
    clique = ...

    Whats = ...
    your = ...
    business = ...
    here = ...

    Sit = ...
    back = ...
    And = ...
    witness = ...
    sheer = ...
    chaos = ...

    You = ...
    cant = ...
    keep = ...
    track = ...
    of = ...
    the = ...
    hell = ...
    we = ...
    Raise = ...

    warning = ...
    this = ...
    escalates = ...
    quickly = ...

    Are = ...
    you = ...
    getting = ...
    nervous = ...

    Are = ...
    you = ...
    getting = ...
    nervous = ...

    The = ...
    mist = ...
    rolls = ...
    In = ...
    thickly = ...

    Are = ...
    you = ...
    getting = ...
    nervous = ...

    Have = ...
    you = ...
    lost = ...
    your = ...
    nerve = ...


def get_words(n: int):
    return SPACE.join(
        random.sample(
            repr(EnterShikari_RabbleRouser_2018()).split(SPACE),
            n
        )
     )


print(get_words(TEN))
