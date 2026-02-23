## Prerequisite

1. Create an account from [Hoppie](https://www.hoppie.nl/acars/system/register.html).
2. Copy the code from your email and paste it into the Hoppie section of the VATPHIL Updater


## Datalink authorities

<table>
  <thead>
    <tr>
      <th style="text-align:center">LOGON</th>
      <th style="text-align:center">Service</th>
      <th style="text-align:center">Callsign</th>
      <th style="text-align:center">Who can use it?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center"><strong>RPLL</strong></td>
      <td style="text-align:center">DCL/PDC</td>
      <td style="text-align:center">MANILA DELIVERY</td>
      <td style="text-align:center">LL_DEL, LL_#_GND, LL_GND, LL_TWR, LL_APP</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLC</strong></td>
      <td style="text-align:center">DCL/PDC</td>
      <td style="text-align:center">CLARK DELIVERY</td>
      <td style="text-align:center">LC_DEL, LC_GND, LC_TWR, LC_APP</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPLB**</strong></td>
      <td style="text-align:center">DCL/PDC</td>
      <td style="text-align:center">SUBIC DELIVERY</td>
      <td style="text-align:center">LB_DEL, LB_GND, LB_TWR</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPVM</strong></td>
      <td style="text-align:center">DCL/PDC</td>
      <td style="text-align:center">MACTAN DELIVERY</td>
      <td style="text-align:center">VM_DEL, VM_GND, VM_TWR, VM_APP</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPMD</strong></td>
      <td style="text-align:center">DCL/PDC</td>
      <td style="text-align:center">DAVAO DELIVERY</td>
      <td style="text-align:center">MD_DEL, MD_GND, MD_TWR, MD_APP</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPHI</strong></td>
      <td style="text-align:center">CPDLC/DCL/PDC</td>
      <td style="text-align:center">MANILA CONTROL</td>
      <td style="text-align:center">MNL_CTR, MNL_X_CTR*</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPHX</strong></td>
      <td style="text-align:center">CPDLC/DCL/PDC</td>
      <td style="text-align:center">MANILA CONTROL</td>
      <td style="text-align:center">To only be used if RPHI is taken</td>
    </tr>
    <tr>
      <td style="text-align:center"><strong>RPHM</strong></td>
      <td style="text-align:center">CPDLC/DCL/PDC</td>
      <td style="text-align:center">MANILA CONTROL</td>
      <td style="text-align:center">To only be used if RPHX is taken</td>
    </tr>
  </tbody>
</table>

**If RPLC_APP is online, approach will use the RPLC logon as LC_APP controls RPLB

*MNL_1, MNL_2, MNL_3, MNL_4, MNL_5, MNL_6, MNL_C, MNL_N, MNL_S, MNL_CE


## Further reading
  
[Message log](https://www.hoppie.nl/acars/system/log.html)  
[Stations online](https://www.hoppie.nl/acars/system/online.html)

