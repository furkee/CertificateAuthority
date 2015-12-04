﻿
import CryptoBox, RSA, utils

from binascii import unhexlify, hexlify

if __name__ == "__main__":
    message = "Hello there! The angel from my nightmare!"

    #e = 3427440831550230275350454123867625763180638697807296205185793806092802022614405471275175335165136699401903167008960184890776241294009495570982302846921194978209932910793857647043824910133564218141662718523229208014146926984783120559169877695555007763530063439102715017904210527646312288623698644098013812365210025137088009748315909639913432925495122323151549450464628617854111440982030094234676636889762204520129523060062291589962740126638097938796124796082493403443067756215517020800579153852237032244637393249376260271091990022822965662254735481326941406651356068562157312028908859161898148492141030155906304452027
    #d = 11516457151875655228726827209706259813249283366592923210502095815616718029466258474052418462212452680117542455638916325361675335957042225433261611017671259916790381417690746551721328810921619790480219932218291995417483840912399177524288561375739425547707367323929570043276158999460590781536103559637265377685704283894273392464196929097819914320872461850922449162251499703236151700073913841608777760982696525272089062714319729133483784645125964885092105823736887970435134921365748478203973468060746832725231004904366492269456708307310623693122874527345936251013791300986665457994631451455921188536602168993793977925063
    #p = 108103761641516353796149491548109377743892534317284571403981703838350160231067325125704414072987121851375651978878681456992993998967031582593521209024411445070914311271863111481716133523093895549454404223183888853604315869650876288188098659269533439017267656293175076542622043099509854827295355491854011975011
    #q = 136301606352578601042790019966255759970626554315990608632231793957406918630338395982650203556572069753926719154023654926017862980056754360839179566490227184077847377258492454138822361826058912824593934004980263447488990492879888093934747350336057164836409349601327495809349758159064349835550842243356799325771
    #N = p * q

    #keys = CryptoBox.RSAencryption(message, 1)

    #e, N, d, p, q, cipher_text = keys[0], keys[1], keys[2], keys[3], keys[4], keys[5]

    #print CryptoBox.RSAdecryption(N, d, p, q, cipher_text)

    keys = CryptoBox.RSAGenerateSignature(message, 1)

    e, N, d, p, q, signature = keys[0], keys[1], keys[2], keys[3], keys[4], keys[5]

    print CryptoBox.RSAVerifySignature(N, e, message, signature)

    ## TODO signature gen - ver does not work