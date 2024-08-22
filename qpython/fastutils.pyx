#
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

#cython: language_level=3


import numpy
cimport numpy as cnp

cnp.import_array()

DTYPE = numpy.intc
ctypedef cnp.int32_t DTYPE_t
DTYPE8 = numpy.uint8
ctypedef cnp.uint8_t DTYPE8_t



def uncompress(const DTYPE8_t[:] compressed, DTYPE_t uncompressed_size):
    _0 = DTYPE(0)
    _1 = DTYPE(1)
    _2 = DTYPE(2)

    cdef DTYPE_t n, r, i, d, s, p, pp, f, m
    n, r, s, p, pp = _0, _0, _0, _0, _0
    i, d = _1, _1

    cdef DTYPE_t[::1] buffer = numpy.zeros(256, dtype = DTYPE)
    cdef DTYPE8_t[::1] uncompressed = numpy.zeros(uncompressed_size, dtype = DTYPE8)

    f = compressed[0]

    while s < uncompressed_size:
        pp = p + 1

        if f & i:
            r = buffer[compressed[d]]
            uncompressed[s] = uncompressed[r]
            uncompressed[s + 1] = uncompressed[r + 1]

            n = compressed[d + 1]

            d += 2
            r += 2
            s += 2

            for m in range(n):
                uncompressed[s + m] = uncompressed[r + m]
        else:
            uncompressed[s] = compressed[d]
            s += 1
            d += 1

        while pp < s:
            buffer[(uncompressed[p]) ^ (uncompressed[pp])] = p
            p = pp
            pp += 1

        if f & i:
            s += n
            p = s

        if i == 128:
            if s < uncompressed_size:
                f = compressed[d]
                d += 1
                i = 1
        else:
            i += i

    return numpy.asarray(uncompressed)
