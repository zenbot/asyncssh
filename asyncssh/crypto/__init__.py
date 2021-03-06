# Copyright (c) 2014-2015 by Ron Frederick <ronf@timeheart.net>.
# All rights reserved.
#
# This program and the accompanying materials are made available under
# the terms of the Eclipse Public License v1.0 which accompanies this
# distribution and is available at:
#
#     http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     Ron Frederick - initial implementation, API, and documentation

"""A shim for accessing cryptographic primitives needed by asyncssh"""

from .cipher import register_cipher, lookup_cipher

from .ec import decode_ec_point, encode_ec_point
from .ec import get_ec_curve_params, lookup_ec_curve_by_params

# Import PyCA versions of DSA, ECDSA, and RSA
from .pyca.dsa import DSAPrivateKey, DSAPublicKey
from .pyca.ec import ECDSAPrivateKey, ECDSAPublicKey
from .pyca.rsa import RSAPrivateKey, RSAPublicKey

# Import pyca module to get ciphers defined there registered
from . import pyca

# Import chacha20-poly1305 cipher if available
from . import chacha

# Import curve25519 DH if available
try:
    from .curve25519 import Curve25519DH
except ImportError: # pragma: no cover
    pass

# Import native Python ECDH module
from .ecdh import ECDH
