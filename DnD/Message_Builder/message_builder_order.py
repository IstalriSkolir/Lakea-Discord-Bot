def dnd_order_message(message_dict):
    key_list = list(message_dict)
    key_list.sort()
    message_list = []
    for key in key_list:
        segments = check_segment_length(message_dict[key])
        for segment in segments:
            message_list.append(segment)
    return message_list

def check_segment_length(segment):
    if(len(segment) <= 2000):
        return [segment]
    else:
        words = segment.split(" ")
        segments = [""]
        current_segment = 0
        for word in words:
            if(len(segments[current_segment]) + len(word) <= 2000):
                segments[current_segment] += f" {word}"
            else:
                current_segment += 1
                segments.append(f" {word}")
        return segments
