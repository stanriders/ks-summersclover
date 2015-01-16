# This is the I-Machine, the flow control script for KS.
# Dedicated to Irina ~<3

# this is the new version. See the old one for documentation.

# Start of the actual script and entry point for a new game. Don't change.
label imachine:
    jump_out C0

# From here on, actual scene labels.

#######################
#     Common path     #
#######################

label C0:
    call iscene ("C0")
    jump_out C1
    
label C1:
    $ tcard(1, "all")
    call iscene ("C1")
    jump_out C2
    
label C2:
    call iscene ("C2")
    jump_out C3
    
label C3:
    call iscene ("C3")
    jump_out C4
    
label C4:
    call iscene ("C4")
    jump_out C5
    
label C5:
    call iscene ("C5")
    jump_out C6

label C6:
    call iscene ("C6")
    jump_out C7
    
label C7:
    call iscene ("C7")
    jump_out C8
    
label C8:
    call iscene ("C8")
    jump_out C9
    
label C9: 
    call iscene ("C9")
    call imenu ("choiceC9")
    if _return == m1:
        call iscene ("C9a")
        jump_out S1
    else:
        call iscene ("C9b")
        jump_out H1

#######################
#      Hisao path     #
#######################

label H1:
    $ tcard(2, "hisao")
    call iscene ("H1")
    jump_out H2

label H2:
    call iscene ("H2")
    jump_out H3

label H3:
    call iscene ("H3")
    jump_out H4

label H4:
    call iscene ("H4")
    jump_out H5

label H5:
    call iscene ("H5")
    jump_out H6
    
label H6:
    call iscene ("H6")
    jump_out H7
    
label H7:
    call iscene ("H7")
    jump_out H8
    
label H8:
    call iscene ("H8")
    jump_out H9
    
label H9:
    call iscene ("H9")
    jump_out H10
    
label H10:
    call iscene ("H10")
    jump_out H11
    
label H11:
    call iscene ("H11")
    call credits
    jump_out restart
    
#######################
#    Suzuki path     #
#######################

label S1:
    $ tcard(2, "suzu")
    call iscene ("S1")
    jump_out S2
    
label S2:
    call iscene ("S2")
    jump_out S3
    
label S3:
    call iscene ("S3")
    jump_out S4
    
label S4:
    call iscene ("S4")
    jump_out S5
    
label S5:
    call iscene ("S5")
    jump_out S6
    
label S6:
    call iscene ("S6")
    jump_out S7
    
label S7:
    call iscene ("S7")
    jump_out S8
    
label S8:
    call iscene ("S8")
    jump_out S9
    
label S9:
    call iscene ("S9")
    jump_out S10
    
label S10:
    call iscene ("S10")
    jump_out S11
    
label S11:
    call iscene ("S11")
    jump_out S12
    
label S12:
    call iscene ("S12")
    jump_out S13
    
label S13:
    call iscene ("S13")
    jump_out S14
    
label S14:
    call iscene ("S14")
    call credits
    jump_out restart
    
