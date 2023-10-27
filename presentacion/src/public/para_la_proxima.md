DESDE AQUI, MUY AVANZADO: HACER PARA CUANDO VOLVAMOS A RETOMAR BUCLES Y CONDICIONALES

---

# Operaciones con booleanos

- Tres operaciones: `NOT`, `AND`, `OR`:


<table>
<tr><th>NOT</th><th>AND</th><th>OR</th></tr>
<tr>
<td>

|a| `not(a)` |
|--|--|
| True | False |
| False | True |

</td><td>

|a|b|`a and b`|
|--|--|--|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |
</td><td>

|a|b|`a or b`|
|--|--|--|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

</td></tr>
</table>

---

# Ejercicio con booleanos

```python
he_robado = ...
me_han_pillado = ...
he_sido_acusado_injustamente = ...
he_sobornado_al_juez = ...
tengo_millones = 0.001
```
<!-- .element style="font-size: 1em" -->
Escribe expresiones booleanas para lo siguiente. `True` es que vas a la carcel:
- Si has robado y te han pillado, vas a la carcel.
- Si has robado, o no has robado pero  has sido acusado injustamente, vas a la carcel
- Si has robado y te han pillado vas a la carcel, excepto si has sobornado al juez
- Si tienes más de 100 millones, no vas a la carcel aunque hayas robado y te hayan pillado
- Si has sobornado al juez y te han pillado, vas a la carcel.
