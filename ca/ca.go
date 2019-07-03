package main

import (
	"bufio"
	"flag"
	"fmt"
	"math"
	"math/rand"
	"os"
	"strings"
	"time"
)

const nΣ = 10
const nΔ = 10

type transition struct {
	source *state
	dest *state
	sym int
	C float32
	P[nΔ] float32
	mark[nΔ] bool
	cond bool
	temp bool
}

type state struct {
	stnum int
	δ[nΣ] *transition
	rew, pun bool
	next *state
}

type exp struct {
	t1, t2 *transition
	E float32
	next *exp
}

type inset[nΔ] float32

var α float32
var β float32
var γ float32
var η float32
var ζ float32
var ν float32
var κ float32

var c *state
var q_a *state
var t_m1, t_m2 *transition
var o_l int
var o int
var so float32
var I_m1, I_m2 *inset
var Q *state
var E *exp
var nstate int
var debug bool

func main() {
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "%s [flags] config\n", os.Args[0])
		flag.PrintDefaults()
	}
	flag.BoolVar(&debug, "d", false, "turn on debugging output")
	flag.Parse()
	if flag.Arg(0) == "" {
		flag.Usage()
	}
	procconfig(flag.Arg(0))
	q0 := mkstate()
	q1 := mkstate()
	q2 := mkstate()
	t := mktrans(q0, q1, 1, 1000000.0, false)
	t.P[1] = 1.0
	q0.δ[1] = t
	t = mktrans(q1, q2, 2, 1000000.0, false)
	t.P[0] = 1.0
	q1.δ[2] = t
	t = mktrans(q2, q0, 0, 1000000.0, false)
	t.P[0] = 1.0
	q2.δ[0] = t
	if debug {
		dump()
	}
	now := time.Now()
	rand.Seed(now.UnixNano())
	c = q0
	q_a = c
	t_m1 = nil
	t_m2 = nil
	o = 0
	o_l = 0
	I_m1 = new(inset)
	I_m2 = new(inset)
	br := bufio.NewReader(os.Stdin)
	for {
		inline, err := br.ReadString('\n')
		if err != nil {
			break
		}
		if inline[0] == 'D' {
			dump()
		} else {
			i := parseinput(inline)
			step(i)
			fmt.Println(o, so)
		}
	}
}

func procconfig(cf string) {
	fd, err := os.Open(cf)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	bc := bufio.NewReader(fd)
	s, _ := bc.ReadString('\n')
	fmt.Sscan(s, &α)
	s, _ = bc.ReadString('\n')
	fmt.Sscan(s, &β)
	s, _ = bc.ReadString('\n')
	fmt.Sscan(s, &γ)
	s, _ = bc.ReadString('\n')
	fmt.Sscan(s, &η)
	s, _ = bc.ReadString('\n')
	fmt.Sscan(s, &ζ)
	s, _ = bc.ReadString('\n')
	fmt.Sscan(s, &ν)
	s, _ = bc.ReadString('\n')
	fmt.Sscan(s, &κ)
	if debug {
		fmt.Println("alpha =", α)
		fmt.Println("beta =", β)
		fmt.Println("gamma =", γ)
		fmt.Println("eta =", η)
		fmt.Println("zeta =", ζ)
		fmt.Println("nu =", ν)
		fmt.Println("kappa =", κ)
	}
}

func parseinput(s string) *inset {
	var sym int
	var str float32

	i := new(inset)
	inlist := strings.Split(s, " ")
	for _, inp := range inlist {
		fmt.Sscanf(inp, "%d/%f", &sym, &str)
		if debug {
			fmt.Println("input ", sym, "with strength", str)
		}
		i[sym] = str
	}	
	return i
}

func dump() {
	dumpmach(Q)
	for e := E; e != nil; e = e.next {
		if e.t1 == nil || e.t2 == nil {
			fmt.Fprintln(os.Stderr, "nil pointer in E", e.t1, e.t2)
		}
		fmt.Fprint(os.Stderr, "E(", e.t1.source.stnum, ",", e.t1.sym, ",",
			e.t2.source.stnum, ",", e.t2.sym, ") = ", e.E, "\n")
	}
}

func dumpmach(q *state) {
	if q == nil {
		return
	}
	dumpmach(q.next)
	fmt.Fprintln(os.Stderr, "q", q.stnum, "  R:", q.rew, "   P:", q.pun)
	for a := 0; a < nΣ; a++ {
		t := q.δ[a]
		if t != nil {
			fmt.Fprintln(os.Stderr, "\tdelta(", q.stnum, ",", a, ")=", t.dest.stnum,
				"C:", t.C, " cond:", t.cond, " temp:", t.temp)
			fmt.Fprint(os.Stderr, "\t\tP: ")
			for b := 0; b < nΔ; b++ {
				fmt.Fprint(os.Stderr, t.P[b], " ")
			}
			fmt.Fprintln(os.Stderr)
		}
	}
}

func step(I *inset) {
	if I[0] > 0.0001 {
		t := c.δ[0]
		if t != nil {
			t.temp = false
			c = t.dest
		}
		q_a = c
		o_l = o
		o = 0
		app_cond(0, 1.0)
		for q := Q; q != nil; q = q.next {
			for a := 0; a < nΣ; a++ {
				for b := 0; b < nΔ; b++ {
					if q.δ[a] != nil {
						q.δ[a].mark[b] = false
					}
				}
			}
		}
		t_m2 = nil
		t_m1 = nil
		I_m1 = new(inset)
		I_m2 = new(inset)
		return
	}
	a_d := 0
	s_d := float32(0.0)
	for a := 0; a < nΣ; a++ {
		if I[a] > s_d {
			a_d = a
			s_d = I[a]
		}
	}
	createt(I)
	t := c.δ[a_d]
	o_l = o
	o = λ(t)
	so = s_d * t.C / (1.0 + t.C)
	t.mark[o] = true
	updateE(I, a_d)
/*
	if c.rew {
		reward()
	} else if c.pun {
		punish()
	}
*/
	if o_l != 0 && o != o_l {
		app_cond(a_d, s_d)
	}
	c = t.dest
	I_m2 = I_m1
	I_m1 = I
	t_m2 = t_m1
	t_m1 = t
}

func createt(I *inset) {
	if c.δ[0] != nil && c.δ[0].temp {
		c.δ[0] = nil
	}
	for i := 1; i < nΣ; i++ {
		if I[i] > 0.0001 {
			if c.δ[i] == nil {
				qn := mkstate()
				qp := lookuptrans(i)
				c.δ[i] = mktrans(c, qn, i, 0.1, false)
				qn.δ[0] = mktrans(qn, q_a, 0, 1.0, true)
				qn.δ[0].P[0] = 1.0
				if qp != nil {
					copy(c.δ[i].P[:], qp.δ[i].P[:])
					c.δ[i].C = qp.δ[i].C
					qn.rew = qp.rew
					qn.pun = qp.pun
					e := new(exp)
					e.t1 = c.δ[i]
					e.t2 = qp.δ[i]
					e.next = E
					E = e
					e = new(exp)
					e.t1 = qp.δ[i]
					e.t2 = c.δ[i]
					e.next = E
					E = e
				} else {
					c.δ[i].P[0] = η
					x := (1.0 - η) / (nΔ - 1)
					for b := 1; b < nΔ; b++ {
						c.δ[i].P[b] = x
					}
				}
			}
		}
	}
}

func updateE(I *inset, a_d int) {
	var e *exp

	if t_m1 != nil {
		q_l := t_m1.source
		a_l := t_m1.sym
		e = findE(q_l, a_l, c, a_d)
		if e != nil {
			ΔE := α * (1.0 - e.E)
			e.E += ΔE
			q_l.δ[a_l].C *= 1.0 - β * abs32(ΔE)
			e = findE(c, a_d, q_l, a_l)
			ΔE = α * (1.0 - e.E)
			e.E += ΔE
			c.δ[a_d].C *= 1.0 - β * abs32(ΔE)
		} else if a_l != 0 {
			e = new(exp)
			e.t1 = q_l.δ[a_l]
			e.t2 = c.δ[a_d]
			e.E = α
			e.next = E
			E = e
			e = new(exp)
			e.t1 = c.δ[a_d]
			e.t2 = q_l.δ[a_l]
			e.E = α
			e.next = E
			E = e
			if debug {
				fmt.Printf("Creating E(%d,%d,%d,%d)\n",
					q_l.stnum, a_l, c.stnum, a_d)
			}
		}
		for a := 1; a < nΣ; a++ {
			if I[a] < 0.0001 {
				e = findE(q_l, a_l, c, a)
				if e != nil {
					ΔE := -α * e.E
					e.E += ΔE
					q_l.δ[a_l].C *= 1.0 - β * abs32(ΔE)
					e = findE(c, a, q_l, a_l)
					ΔE = -α * e.E
					e.E += ΔE
					c.δ[a].C *= 1.0 - β * abs32(ΔE)
				}
			}
		}
		for q := Q; q != nil; q = q.next {
			for a := 1; a < nΣ; a++ {
				if (q != q_l || a != a_l) && q.δ[a] != nil {
					e = findE(c, a_d, q, a)
					if e != nil {
						ΔE := -α * e.E
						e.E += ΔE
						c.δ[a_d].C *= 1.0 - β * abs32(ΔE)
						e = findE(q, a, c, a_d)
						ΔE = -α * e.E
						e.E += ΔE
						q.δ[a].C *= 1.0 - β * abs32(ΔE)
					}
				}
			}
		}
	}
	for a := 1; a < nΣ; a++ {
		for b := 1; b < nΣ; b++ {
			if a != b {
				if I[a] > 0.0001 && I[b] > 0.0001 {
					e = findE(c, a, c, b)
					if e != nil {
						ΔE := α * (1.0 - e.E)
						e.E += ΔE
						c.δ[a].C *= 1.0 - β * abs32(ΔE)
					} else {
						if c.δ[a] != nil && c.δ[b] != nil {
							e = new(exp)
							e.t1 = c.δ[a]
							e.t2 = c.δ[b]
							e.E = α
							e.next = E
							E = e
						}
					}
				} else if I[a] > 0.0001 || I[b] > 0.0001 {
					e = findE(c, a, c, b)
					if e != nil {
						ΔE := -α * e.E
						e.E += ΔE
						c.δ[a].C *= 1.0 - β * abs32(ΔE)
					}
				}
			} 
		}
	}
}

/*
func reward() {
	t := 1.0
	for q := Q; q != nil; q = q.next {
		for a := 0; a < nΣ; a++ {
			if q.δ[a] != nil {
				for o := 0; o < nΔ; n++ {
					if q.δ[a].mark[o] {
					}
				}
			}
		}
	}
}
*/

func app_cond(a_d int, s_d float32) {
	if t_m1 == nil {
		return
	}
	q_l := t_m1.source
	a_l := t_m1.sym
	if debug {
		fmt.Fprint(os.Stderr, "Conditioning: c=", c.stnum, " a_d=", a_d,
			" q_l=", q_l.stnum, " a_l=", a_l, " o_l=", o_l, " I-2=", I_m2, "\n")
	}
	for q := Q; q != nil; q = q.next {
		for a := 1; a < nΣ; a++ {
			if q.δ[a] != nil {
				q.δ[a].cond = false
			}
		}
	}
	for a := 1; a < nΣ; a++ {
		if I_m1[a] > 0.0001 && q_l.δ[a] != nil {
			e := findE(q_l, a_l, q_l, a)
			if e != nil {
				for b := 0; b < nΔ; b++ {
					if b == o_l {
						q_l.δ[a].P[b] = incprob(q_l, a, s_d, b)
					} else {
						q_l.δ[a].P[b] = decprob(q_l, a, s_d, b)
					}
				}
			}
		}
	}
	for q := Q; q != nil; q = q.next {
		for a := 1; a < nΣ; a++ {
			if q.δ[a] != nil && q.δ[a].dest == q_l {
				e := findE(q_l, a_l, q, a)
				if e != nil {
					for b := 0; b < nΔ; b++ {
						if b == o_l {
							q.δ[a].P[b] = incprob(q, a, s_d, b)
						} else {
							q.δ[a].P[b] = decprob(q, a, s_d, b)
						}
					}
				}
			}
		}
	}
	for a := 1; a < nΣ; a++ {
		if I_m1[a] > 0.0001 && q_l.δ[a] != nil && !(q_l.δ[a].cond) {
			e := findE(q_l, a_l, q_l, a)
			if e != nil {
				if !(q_l.δ[a].cond) {
					q_l.δ[a].C += γ * s_d
					q_l.δ[a].cond = true
					updcond(q_l, a, s_d / q_l.δ[a].C)
				}
			}
		}
	}
	for q := Q; q != nil; q = q.next {
		for a := 1; a < nΣ; a++ {
			if q.δ[a] != nil && q.δ[a].dest == q_l && !(q.δ[a].cond) {
				e := findE(q_l, a_l, q, a)
				if e != nil {
					if !(q.δ[a].cond) {
						q.δ[a].C += γ * s_d
						q.δ[a].cond = true
						updcond(q, a, s_d / q.δ[a].C)
					}
				}
			}
		}
	}
}

func updcond(qp *state, ap int, s float32) {
	if s <= 0.0001 {
		return
	}
	if debug {
		fmt.Fprint(os.Stderr, "Propagating conditioning qp=", qp.stnum, " ap=", ap, "\n")
	}
	for a := 1; a < nΣ; a++ {
		if qp.δ[a] != nil && !(qp.δ[a].cond) {
			e := findE(qp, ap, qp, a)
			if e != nil {
				for b := 0; b < nΔ; b++ {
					if b == o_l {
						qp.δ[a].P[b] = incprob(qp, a, s, b)
					} else {
						qp.δ[a].P[b] = decprob(qp, a, s, b)
					}
				}
			}
		}
	}
	for q := Q; q != nil; q = q.next {
		for a := 1; a < nΣ; a++ {
			if q.δ[a] != nil && q.δ[a].dest == qp && !(q.δ[a].cond) {
				e := findE(qp, ap, q, a)
				if e != nil {
					for b := 0; b < nΔ; b++ {
						if b == o_l {
							q.δ[a].P[b] = incprob(q, a, s, b)
						} else {
							q.δ[a].P[b] = decprob(q, a, s, b)
						}
					}
				}
			}
		}
	}
	for a := 1; a < nΣ; a++ {
		if /* I_m1[a] > 0.0001 && */ qp.δ[a] != nil && !(qp.δ[a].cond) {
			e := findE(qp, ap, qp, a)
			if e != nil {
				qp.δ[a].C += γ * s
				qp.δ[a].cond = true
				updcond(qp, a, s / qp.δ[a].C)
			}
		}
	}
	for q := Q; q != nil; q = q.next {
		for a := 1; a < nΣ; a++ {
			if q.δ[a] != nil && q.δ[a].dest == qp && !(q.δ[a].cond) {
				e := findE(qp, ap, q, a)
				if e != nil {
					q.δ[a].C += γ * s
					q.δ[a].cond = true
					updcond(q, a, s / q.δ[a].C)
				}
			}
		}
	}
}

func incprob(q *state, a int, s float32, o int) float32 {
	x := ( γ * s ) / q.δ[a].C
	return (q.δ[a].P[o] +  x) / (1.0 + x)
}

func decprob(q *state, a int, s float32, o int) float32 {
	x := ( γ * s ) / q.δ[a].C
	return q.δ[a].P[o] / (1.0 + x)
}

func abs32(x float32) float32 {
	return float32(math.Abs(float64(x)))
}

func findE(q1 *state, a1 int, q2 *state, a2 int) *exp {
	t1 := q1.δ[a1]
	t2 := q2.δ[a2]
	if t1 == nil || t2 == nil {
		return nil
	}
	for e := E; e != nil; e = e.next {
		if e.t1 == t1 && e.t2 == t2 {
			return e
		}
	}
	return nil
}

func mktrans(src *state, dest *state, sym int, C float32, temp bool) *transition {
	t := new(transition)
	t.source = src
	t.dest = dest
	t.sym = sym
	t.C = C
	t.temp = temp
	return t
}

func mkstate() *state {
	s := new(state)
	s.stnum = nstate
	nstate++
	s.next = Q
	Q = s
	return s
}

func λ(t *transition) int {
	x := rand.Float32()
	for i := 0; i < nΔ; i++ {
		if x < t.P[i] {
			return i
		}
		x -= t.P[i]
	}
	return 0
}

func lookuptrans(sym int) *state {
	for q := Q; q != nil; q = q.next {
		if q.δ[sym] != nil {
			return q
		}
	}
	return nil
}
