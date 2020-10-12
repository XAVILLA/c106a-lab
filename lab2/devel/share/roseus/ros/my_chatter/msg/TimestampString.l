;; Auto-generated. Do not edit!


(when (boundp 'my_chatter::TimestampString)
  (if (not (find-package "MY_CHATTER"))
    (make-package "MY_CHATTER"))
  (shadow 'TimestampString (find-package "MY_CHATTER")))
(unless (find-package "MY_CHATTER::TIMESTAMPSTRING")
  (make-package "MY_CHATTER::TIMESTAMPSTRING"))

(in-package "ROS")
;;//! \htmlinclude TimestampString.msg.html


(defclass my_chatter::TimestampString
  :super ros::object
  :slots (_s _f ))

(defmethod my_chatter::TimestampString
  (:init
   (&key
    ((:s __s) "")
    ((:f __f) 0.0)
    )
   (send-super :init)
   (setq _s (string __s))
   (setq _f (float __f))
   self)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:f
   (&optional __f)
   (if __f (setq _f __f)) _f)
  (:serialization-length
   ()
   (+
    ;; string _s
    4 (length _s)
    ;; float64 _f
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _s
       (write-long (length _s) s) (princ _s s)
     ;; float64 _f
       (sys::poke _f (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _s
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _s (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _f
     (setq _f (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_chatter::TimestampString :md5sum-) "bb650c4713fc5c9f7ae69948f3e9e0f2")
(setf (get my_chatter::TimestampString :datatype-) "my_chatter/TimestampString")
(setf (get my_chatter::TimestampString :definition-)
      "string s
float64 f

")



(provide :my_chatter/TimestampString "bb650c4713fc5c9f7ae69948f3e9e0f2")


