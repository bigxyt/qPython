#  Copyright (c) 2011-2014 Exxeleron GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import numpy

DTYPE = numpy.intc
DTYPE8 = numpy.uint8

def uncompress(compressed, uncompressed_size):
    _0 = DTYPE(0)
    _1 = DTYPE(1)
    _2 = DTYPE(2)
    _128 = DTYPE(128)
    _255 = DTYPE(255)

    n, r, s, p = _0, _0, _0, _0
    i, d = _1, _1
    f = _255 & compressed[_0]

    buffer = numpy.zeros(256, dtype = DTYPE)
    uncompressed = numpy.zeros(uncompressed_size, dtype = DTYPE8)
    idx = numpy.arange(uncompressed_size, dtype = DTYPE)

    while s < uncompressed_size:
        pp = p + _1

        if f & i:
            r = buffer[compressed[d]]
            n = _2 + compressed[d + _1]
            uncompressed[idx[s:s + n]] = uncompressed[r:r + n]

            buffer[(uncompressed[p]) ^ (uncompressed[pp])] = p
            if s == pp:
                buffer[(uncompressed[pp]) ^ (uncompressed[pp + _1])] = pp

            d += _2
            r += _2
            s = s + n
            p = s

        else:
            uncompressed[s] = compressed[d]

            if pp == s:
                buffer[(uncompressed[p]) ^ (uncompressed[pp])] = p
                p = pp

            s += _1
            d += _1

        if i == _128:
            if s < uncompressed_size:
                f = _255 & compressed[d]
                d += _1
                i = _1
        else:
            i += i

    return uncompressed
