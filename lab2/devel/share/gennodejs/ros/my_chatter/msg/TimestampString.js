// Auto-generated. Do not edit!

// (in-package my_chatter.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TimestampString {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.s = null;
      this.f = null;
    }
    else {
      if (initObj.hasOwnProperty('s')) {
        this.s = initObj.s
      }
      else {
        this.s = '';
      }
      if (initObj.hasOwnProperty('f')) {
        this.f = initObj.f
      }
      else {
        this.f = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TimestampString
    // Serialize message field [s]
    bufferOffset = _serializer.string(obj.s, buffer, bufferOffset);
    // Serialize message field [f]
    bufferOffset = _serializer.float64(obj.f, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TimestampString
    let len;
    let data = new TimestampString(null);
    // Deserialize message field [s]
    data.s = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [f]
    data.f = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.s.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'my_chatter/TimestampString';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bb650c4713fc5c9f7ae69948f3e9e0f2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string s
    float64 f
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TimestampString(null);
    if (msg.s !== undefined) {
      resolved.s = msg.s;
    }
    else {
      resolved.s = ''
    }

    if (msg.f !== undefined) {
      resolved.f = msg.f;
    }
    else {
      resolved.f = 0.0
    }

    return resolved;
    }
};

module.exports = TimestampString;
