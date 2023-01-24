import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadListings } from '../../store/listings';
import './Homepage.css';
import star from '../../icons/homepage/cardstar.svg';

const Homepage = () => {
    const dispatch = useDispatch();
    const listingList = useSelector(state => state.listings.allListings);
    const listings = listingList ? Object.values(listingList) : null;
    const type = useSelector(state => state.listings.type);
    console.log('this is the type', type);

    const puns = [
        'Prepare for fun',
        'With room to spare',
        'Nothing else compares',
        'The perfect pairing for your trip',
        'Comfort paired with lots of fun'
    ]

    useEffect(() => {
        dispatch(loadListings(type));
    }, [type, dispatch]);


    if (!Object.keys(listingList).length) {
        return (
            <div className='main-homepage-container'>
                <div className='empty-list-container'>
                    <h1 className='empty-list-title'>It appears that there are no listings that match your selection(s).<br /></h1>
                </div>
            </div>
        )
    }

    return (
    <div className='main-homepage-container-outer'>
        {/* {typesSection} */}
      <div className='main-homepage-container'>
          <div className='main-card-container'>
          {listings.map((listing, i) => (
            <a key={i} className='listing-card-link' href={`/listings/${listing.id}`}>
                <div className='listing-card'>
                    <div className='listing-card-innertop'>
                        <img src={listing?.images?.[0]} alt='listing' className='listing-image-preview' onError={e => e.currentTarget.src = 'https://i.imgur.com/DsVjt4A.png'}/>
                    </div>
                    <div className='listing-card-innerbottom'>
                        <div className='listing-card-info'>
                            <div className='listing-info-location listing-info'>
                                {listing.city}, {listing.state}
                            </div>
                            <div className='listing-info-distance listing-info'>
                                {puns[Math.floor(Math.random() * puns.length)]}
                            </div>
                            <div className='listing-info-cost'>
                                <span className='cost-dollars'>${listing.price} </span>
                                <span className='cost-night'>night</span>
                            </div>
                        </div>
                        <div className='listing-card-rating'>
                            <span className='listing-rating-star'>
                                <img src={star} alt='star' />
                            </span>
                            <span className='listing-rating-avg'>
                                {listing?.avg_rating > 0 ? listing.avg_rating.toFixed(1) : 'New'}
                            </span>
                        </div>
                    </div>
                </div>
            </a>
          ))}
          </div>
      </div>
      </div>
    )
}

export default Homepage;
