#!/usr/bin/env gsi
(define (parse-deck)
	(read-line) ; no-op
	(let read-until-empty ()
		(let [(line (read-line))]
			(if (or (equal? line "") (equal? line #!eof))
				'()
				(cons (string->number line) (read-until-empty))))))


(define deck (list (parse-deck) (parse-deck)))

(define (fight deck)
	; (println (object->string deck))
	(let [(player1 (cdar deck))
	      (draw1 (caar deck))
	      (player2 (cdadr deck))
	      (draw2 (caadr deck))]
		(if
			(if (and (>= (length player1) draw1) (>= (length player2) draw2))
				(null? (car (game (list
					(take player1 draw1)
					(take player2 draw2)))))
				(< draw1 draw2))
			(list player1 (append player2 (list draw2 draw1)))
			(list (append player1 (list draw1 draw2)) player2))))


(define (game deck #!optional (seen (make-table)))
	(let* [(player1 (car deck)) (player2 (cadr deck)) (hash (equal?-hash player1))]
		(if (or (null? player1) (null? player2) (table-ref seen hash #f))
			deck
			(game (fight deck) (begin (table-set! seen hash #t) seen)))))


(define (winner deck)
	(let [(player1 (car deck)) (player2 (cadr deck))]
		(if (null? player1) player2 player1)))

(define (score deck #!optional (index 1))
	(if (null? deck)
		0
		(+ (* (car deck) index) (score (cdr deck) (+ index 1)))))

(println (score (reverse (winner (game deck)))))
