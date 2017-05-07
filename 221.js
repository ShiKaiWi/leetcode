let memorizer = {};
function memorize(m,x,y,length) {
    let key = `${x}-${y}-${length}`;
    if (!(key in memorizer)) {
        memorizer[key] = helper(m,x,y,length);
    }
    return memorizer[key];
}

function helper(m, x, y, length) {
    let l = length - 1;
    if ( length<1 ) {
        return 0;
    }
    if ( length===1) {
        if (m[x][y] === '1') {
            return 1;
        } else {
            return 0;
        }
    }
    let l1 = memorize(m, x, y, l);
    let l2 = memorize(m, x+1, y, l);
    let l3 = memorize(m, x, y+1, l);
    let l4 = memorize(m, x+1, y+1, l);
    if( [l1, l2, l3, l4].reduce((acc, d)=>acc && d===l, true)) {
        return length;
    } else {
        return [l1, l2, l3, l4].reduce((acc, d) => acc>d ? acc:d);
    }
}

function helperOuter(mOriginal) {
    let x = mOriginal.length;
    if( mOriginal[0]===undefined) {
        return 0;
    }
    let y = mOriginal[0].length;
    let m = mOriginal.map((data)=>Array.from(data));
    let res = 0;
    if (x>y) {
        for(let i=0;i<=x-y;i++) {
            let t = memorize(m, i, 0, y);
            if (res < t) {
                res = t;
            }
        }
    } else {
        for(let i=0;i<=y-x;i++) {
            let t = memorize(m, 0, i, x);
            if (res < t) {
                res = t;
            }
        }
    }
    return res;
};
var maximalSquare = function(matrix) {
    
    let l = helperOuter(matrix);
    return l*l;
};
