# coding: utf8
from __future__ import unicode_literals

import ujson

from ...util import get_lang_class
from .._messages import Messages


def ner_jsonl2json(input_data, lang=None, n_sents=10, use_morphology=False):
    if lang is None:
        raise ValueError(Messages.M054)
    json_docs = []
    input_tuples = [ujson.loads(line) for line in input_data]
    nlp = get_lang_class(lang)()
    for i, (raw_text, ents) in enumerate(input_tuples):
        doc = nlp.make_doc(raw_text)
        doc[0].is_sent_start = True
        doc.ents = [doc.char_span(s, e, label=L) for s, e, L in ents["entities"]]
        json_docs.append(doc.to_json())
    return json_docs
