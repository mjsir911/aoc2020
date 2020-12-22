(define (parse-deck)
	(read-line) ; no-op
	(let read-until-empty ()
		(let [(line (read-line))]
			(if (or (equal? line "") (equal? line #!eof))
				'()
				(cons (string->number line) (read-until-empty))))))


(define deck (list (parse-deck) (parse-deck)))

(define (fight deck)
	(let [(player1 (car deck))
	      (player2 (cadr deck))]
		(if (< (car player1) (car player2))
			(list (cdr player1) (append (cdr player2) (list (car player2) (car player1))))
			(list (append (cdr player1) (list (car player1) (car player2))) (cdr player2)))))

(define (game deck)
	(if (or (null? (car deck)) (null? (cadr deck)))
		(if (null? (car deck)) (cadr deck) (car deck))
		(game (fight deck))))

(define (score deck #!optional (index 1))
	(if (null? deck)
		0
		(+ (* (car deck) index) (score (cdr deck) (+ index 1)))))

(println (score (reverse (game deck))))
