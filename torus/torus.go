package main

import (
	"fmt"
	"math"
	"os"
	"strings"

	"golang.org/x/term"
)

func main() {
	width, height, err := term.GetSize(int(os.Stdout.Fd()))
	if err != nil {
		width, height = 378, 48
	}

	rx, ry := 60.0, 30.0
	var A, B float64

	// Скрываем курсор
	fmt.Print("\x1b[?25l")
	defer fmt.Print("\x1b[?25h") // Покажем курсор при выходе

	for {
		z := make([]float64, width*height)
		b := make([]rune, width*height)
		for i := range b {
			b[i] = ' '
		}

		for j := 0; j < 628; j += 7 {
			for i := 0; i < 628; i += 2 {
				phi := float64(j) / 100.0
				theta := float64(i) / 100.0

				c := math.Sin(theta)
				d := math.Cos(phi)
				e := math.Sin(A)
				f := math.Sin(phi)
				g := math.Cos(A)
				h := d + 2.0
				D := 1.0 / (c*h*e + f*g + 5.0)
				l := math.Cos(theta)
				m := math.Cos(B)
				n := math.Sin(B)
				t := c*h*g - f*e

				x := int(float64(width)/2.0 + rx*D*(l*h*m - t*n))
				y := int(float64(height)/2.0 + ry*D*(l*h*n + t*m))
				o := x + width*y

				N := int(8.0 * ((f*e - c*d*g)*m - c*d*e - f*g + l*d*n))
				if x >= 0 && x < width && y >= 0 && y < height && D > z[o] {
					z[o] = D
					shades := ".,-~:;=!*#$@"
					if N < 0 {
						N = 0
					}
					if N >= len(shades) {
						N = len(shades) - 1
					}
					b[o] = rune(shades[N])
				}
			}
		}

		var sb strings.Builder
		sb.WriteString("\x1b[H") // переместить курсор в левый верхний угол
		for row := 0; row < height; row++ {
			start := row * width
			sb.WriteString(string(b[start : start+width]))
			sb.WriteByte('\n')
		}
		fmt.Print(sb.String())

		A += 0.04
		B += 0.02
	}
}
