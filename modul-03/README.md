# Modul [03] - Trigonometri

**Nama:** Desintan Feby Harum Saragih  
**NIM:** 1306625071
**Kelas:** Fisika C

---

## 1. Problem Statement
> Membuat program untuk menghitung nilai sin dan cos dengan pendekatan deret meclaurin

## 2. Mathematical Equation
> Deret Maclaurin Umum: f(x) = $$\sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

> Deret Maclaurin untuk $\sin(x)$: $$\sin(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots$$

> Deret Maclaurin untuk $\cos(x)$: $$\cos(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots$$

> Rumus Relative error (Er): $$\varepsilon_r$$ = $$\left| \frac{TV - AV}{TV} \right| \times 100%\%$$
> 

## 3. Algorithm
> Tuliskan langkah-langkah logika penyelesaian masalah secara sistematis sebelum diimplementasikan ke dalam kode Python (`main.py`).
