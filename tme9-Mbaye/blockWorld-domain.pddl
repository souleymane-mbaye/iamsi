(define (domain blockWorld)
        (:requirements :strips :typing)
        (:types block)
        (:predicates
            (on ?x -block ?y -block)
            (ontable ?x - block)
            (clear ?x - block)
            (handempty)
            (holding ?x - block))
        (:action pick-up
            :parameters(?x - block)
            :precondition(and (clear ?x) (ontable ?x) (handempty))
            :effect(and (not (ontable ?x))
                        (not (clear ?x))
                        (not (handempty))
                        (holding ?x)))
        (:action putdown
            :parameters(?x - block)
            :precondition(and (holding ?x))
            :effect(and (not (holding ?x))
                         (ontable ?x)
                         (handempty)
                         (clear ?x)))
        (:action unstack
            :parameters(?x - block ?y - block)
            :precondition(and (on ?x ?y) (handempty) (clear ?x))
            :effect(and (not (on ?x ?y))
                        (not (handempty))
                        (not (clear ?x))
                        (clear ?x)
                        (holding ?x)))
        (:action stack
            :parameters(?x - block ?y - block)
            :precondition(and (clear ?y) (holding ?x))
            :effect(and (not (clear ?y))
                        (not (holding ?x))
                        (on ?x ?y)
                        (clear ?x)
                        (handempty))))
